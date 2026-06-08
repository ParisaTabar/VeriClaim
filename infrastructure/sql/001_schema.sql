-- =============================================================================
-- VeriClaim Academic Schema v0.1
-- Research Decision Support System for scientific claim verification
-- =============================================================================

CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE SCHEMA IF NOT EXISTS sovereign_pipeline;
SET search_path TO sovereign_pipeline, public;

DROP VIEW IF EXISTS latest_verifications;
DROP TABLE IF EXISTS verifications CASCADE;
DROP TABLE IF EXISTS claims CASCADE;
DROP TABLE IF EXISTS articles CASCADE;
DROP TYPE IF EXISTS verification_verdict CASCADE;
DROP TYPE IF EXISTS processing_state CASCADE;

CREATE TYPE processing_state AS ENUM (
    'raw',
    'extracting',
    'extracted',
    'verifying',
    'finalized',
    'failed'
);

CREATE TYPE verification_verdict AS ENUM (
    'supported',
    'refuted',
    'mixed',
    'insufficient_evidence'
);

CREATE TABLE articles (
    id BIGSERIAL PRIMARY KEY,
    external_id UUID DEFAULT uuid_generate_v4() UNIQUE NOT NULL,

    source_identifier VARCHAR(100) NOT NULL DEFAULT 'openalex',
    title TEXT NOT NULL,
    content_hash CHAR(64) UNIQUE NOT NULL,
    canonical_url TEXT,
    doi TEXT,

    abstract TEXT,
    raw_body TEXT,
    authors TEXT,
    publication_year INTEGER,
    scientific_domain TEXT DEFAULT 'General Sciences',
    keywords TEXT,
    citations_count INTEGER DEFAULT 0 CHECK (citations_count >= 0),
    is_open_access BOOLEAN DEFAULT FALSE,

    metadata JSONB DEFAULT '{}'::jsonb,
    language_code CHAR(2) DEFAULT 'en',
    current_status processing_state DEFAULT 'raw',
    error_logs JSONB DEFAULT '[]'::jsonb,

    published_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT article_title_min_length CHECK (char_length(title) > 5),
    CONSTRAINT article_publication_year_range CHECK (
        publication_year IS NULL OR publication_year BETWEEN 1800 AND 2200
    )
);

CREATE TABLE claims (
    id BIGSERIAL PRIMARY KEY,
    external_id UUID DEFAULT uuid_generate_v4() UNIQUE NOT NULL,
    article_id BIGINT NOT NULL REFERENCES articles(id) ON DELETE CASCADE,

    statement TEXT NOT NULL,
    category TEXT DEFAULT 'N/A',
    tags JSONB DEFAULT '[]'::jsonb,
    extraction_model VARCHAR(80) NOT NULL DEFAULT 'llama-3.1-8b-instant',
    extraction_confidence NUMERIC(4, 3) DEFAULT 0.000 CHECK (
        extraction_confidence >= 0 AND extraction_confidence <= 1
    ),

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT claim_statement_min_length CHECK (char_length(statement) > 2),
    CONSTRAINT claims_article_statement_unique UNIQUE (article_id, statement)
);

CREATE TABLE verifications (
    id BIGSERIAL PRIMARY KEY,
    external_id UUID DEFAULT uuid_generate_v4() UNIQUE NOT NULL,
    claim_id BIGINT NOT NULL REFERENCES claims(id) ON DELETE CASCADE,

    verdict verification_verdict DEFAULT 'insufficient_evidence',
    reliability_score SMALLINT DEFAULT 0 CHECK (
        reliability_score >= 0 AND reliability_score <= 100
    ),
    verdict_summary TEXT,
    supporting_evidence JSONB DEFAULT '[]'::jsonb,
    verification_model VARCHAR(80) NOT NULL DEFAULT 'llama-3.1-8b-instant',
    execution_time_ms INTEGER,

    verified_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT verifications_claim_model_unique UNIQUE (claim_id, verification_model)
);

-- JSONB indexes for flexible academic metadata and evidence vectors.
CREATE INDEX idx_articles_metadata_gin ON articles USING GIN (metadata);
CREATE INDEX idx_verifications_evidence_gin ON verifications USING GIN (supporting_evidence);

-- Trigram indexes support fuzzy title and claim search in the Streamlit UI.
CREATE INDEX idx_articles_title_trgm ON articles USING GIN (title gin_trgm_ops);
CREATE INDEX idx_claims_statement_trgm ON claims USING GIN (statement gin_trgm_ops);

-- Queue and relational lookup indexes.
CREATE INDEX idx_articles_pending_task ON articles(current_status)
    WHERE current_status IN ('raw', 'extracting', 'verifying');
CREATE INDEX idx_claims_article_id ON claims(article_id);
CREATE INDEX idx_verifications_claim_id ON verifications(claim_id);
CREATE INDEX idx_verifications_verified_at ON verifications(verified_at DESC);
CREATE INDEX idx_articles_domain_year ON articles(scientific_domain, publication_year DESC);

CREATE OR REPLACE FUNCTION refresh_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_articles_timestamp
BEFORE UPDATE ON articles
FOR EACH ROW EXECUTE FUNCTION refresh_updated_at();

-- Dashboard-ready view: one flat evidence vector per verification.
CREATE VIEW latest_verifications AS
SELECT
    a.id AS article_id,
    a.external_id AS article_external_id,
    a.title,
    a.publication_year,
    a.scientific_domain,
    a.keywords,
    a.citations_count,
    a.authors,
    a.abstract,
    a.doi,
    a.canonical_url,
    a.is_open_access,
    c.id AS claim_id,
    c.statement,
    c.category,
    c.extraction_model,
    c.extraction_confidence AS certainty,
    v.id AS verification_id,
    v.verdict::TEXT AS verdict,
    v.reliability_score AS score,
    v.verdict_summary,
    v.supporting_evidence,
    v.verification_model,
    v.execution_time_ms,
    v.verified_at
FROM articles a
JOIN claims c ON c.article_id = a.id
JOIN verifications v ON v.claim_id = c.id;

COMMENT ON SCHEMA sovereign_pipeline IS 'Research data management schema for VeriClaim academic claim verification.';
COMMENT ON TABLE articles IS 'OpenAlex-derived scientific metadata and reconstructed abstracts used as auditable evidence sources.';
COMMENT ON TABLE claims IS 'Atomic scientific claims extracted from each article by an LLM or NLP model.';
COMMENT ON TABLE verifications IS 'Algorithmic verdicts, reliability scores, and evidence vectors attached to extracted claims.';
COMMENT ON VIEW latest_verifications IS 'Flattened read model used by the Streamlit dashboard and evidence vault.';
