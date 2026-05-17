# SovereignTruth (Project VeriClaim)
### An Autonomous, Cross-Lingual Pipeline for Scientific Claim Verification and Research Data Management

[![Status](https://img.shields.io/badge/Status-Active_Development-g.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-v4.0_Isolated-blue.svg)](#)
[![Database](https://img.shields.io/badge/Database-PostgreSQL_16_Alpine-blue.svg)](#)
[![Engine](https://img.shields.io/badge/Orchestration-n8n_Self--Hosted-orange.svg)](#)

## 📌 Overview
The unchecked proliferation of scientific misinformation and "fake science" poses a critical threat to digital integrity, public policy, and academic communication. **SovereignTruth** is a full-lifecycle, autonomous software and data engineering architecture designed to ingest unstructured academic metadata, parse texts into atomic verifiable claims using Large Language Models (LLMs), and run a multi-factor mathematical scoring matrix to evaluate epistemic certainty and credibility.

By leveraging decentralized orchestration and a highly isolated relational schema, the pipeline completely circumvents black-box commercial infrastructures, prioritizing mathematical reproducibility, strict data lineage, and enterprise-grade data integrity.

---

## ⚙️ System Architecture (v4.0)
The platform is built as a self-hosted, Docker-containerized infrastructure split into a 4-layer functional stack:

1. **Ingestion Layer:** Event-driven automated metadata harvesting utilizing the **OpenAlex API**. Features a custom algorithmic pipeline to dynamically reconstruct text abstracts from inverted token indices.
2. **Semantic Extraction Layer:** Natural Language Processing (NLP) orchestration executing **Llama-3.1-8b-Instant** models via Groq's low-latency API infrastructure to extract objective assertions and determine academic taxonomy classifications.
3. **Verification & Weighting Layer:** A deterministic, multi-factor Python calculation matrix evaluating citation trends, linguistic hedges, and open-science accessibility metrics to output a unified credibility score.
4. **Presentation Layer (In Development):** A minimalist, flat-design **Streamlit** dashboard feeding directly from the isolated database engine for real-time visualization and data auditability.
