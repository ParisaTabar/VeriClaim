import os
from typing import Any, Dict

import pandas as pd
import psycopg2
import streamlit as st
from i18n import tr

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

DB_CONFIG: Dict[str, Any] = {
    "host": os.getenv("POSTGRES_HOST", "db"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "database": os.getenv("POSTGRES_DB", "vericlaim_db"),
    "user": os.getenv("POSTGRES_USER", "vericlaim_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "vericlaim_pass"),
}


@st.cache_data(ttl=30, show_spinner=False)
def load_vault() -> pd.DataFrame:
    sql = """
        SELECT
            verified_at,
            verdict,
            score,
            certainty,
            category,
            scientific_domain,
            publication_year,
            citations_count,
            title,
            statement,
            verdict_summary,
            doi,
            canonical_url
        FROM sovereign_pipeline.latest_verifications
        ORDER BY verified_at DESC;
    """
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            return pd.read_sql_query(sql, conn)
    except Exception as err:
        st.error(f"{tr('vault_load_error')}: {err}")
        return pd.DataFrame()


st.title(tr("vault_title"))
st.caption(tr("vault_subtitle"))

df = load_vault()

if df.empty:
    st.info(tr("no_vault_data"))
    st.stop()

search = st.text_input(
    tr("filter_vault"),
    placeholder=tr("filter_placeholder"),
)

filtered = df.copy()

if search.strip():
    s = search.strip().lower()
    mask = filtered.astype(str).apply(
        lambda col: col.str.lower().str.contains(s, na=False)
    ).any(axis=1)
    filtered = filtered[mask]

display_df = filtered.rename(
    columns={
        "verified_at": tr("verified_at"),
        "verdict": tr("verdict"),
        "score": tr("reliability_index"),
        "certainty": tr("mean_certainty"),
        "category": tr("category"),
        "scientific_domain": tr("domain"),
        "publication_year": tr("publication_year"),
        "citations_count": tr("citations"),
        "title": tr("title"),
        "statement": tr("claim"),
        "verdict_summary": tr("model_rationale"),
        "doi": "DOI",
        "canonical_url": tr("source"),
    }
)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    tr("export_csv"),
    data=csv,
    file_name="vericlaim_vault_export.csv",
    mime="text/csv",
)