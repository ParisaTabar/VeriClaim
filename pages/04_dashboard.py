import os
from typing import Any, Dict

import pandas as pd
import plotly.express as px
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
def load_dashboard_data() -> pd.DataFrame:
    sql = """
        SELECT
            article_id,
            title,
            publication_year,
            scientific_domain,
            citations_count,
            is_open_access,
            statement,
            category,
            certainty,
            verdict,
            score,
            execution_time_ms,
            verified_at
        FROM sovereign_pipeline.latest_verifications
        ORDER BY verified_at DESC
        LIMIT 500;
    """
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            return pd.read_sql_query(sql, conn)
    except Exception as err:
        st.error(f"Could not load dashboard data: {err}")
        return pd.DataFrame()


st.title(tr("dashboard_title"))
st.caption(tr("dashboard_subtitle"))

df = load_dashboard_data()

if df.empty:
    st.info(tr("no_dashboard_data"))
    st.stop()

for col in ["score", "certainty", "citations_count", "execution_time_ms"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

m1, m2, m3, m4 = st.columns(4)
m1.metric(tr("evidence_vectors"), f"{len(df):,}")
m2.metric(tr("mean_reliability"), f"{int(df['score'].mean())}%")
m3.metric(tr("open_access"), f"{int(df['is_open_access'].fillna(False).mean() * 100)}%")
m4.metric(tr("total_citations"), f"{int(df['citations_count'].sum()):,}")

st.divider()

c1, c2 = st.columns(2)

with c1:
    st.subheader(tr("verdict_distribution"))
    fig = px.histogram(df, x="verdict", color="verdict")
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader(tr("domain_distribution"))
    domain_df = df.groupby("scientific_domain", dropna=False).size().reset_index(name="count")
    fig = px.pie(domain_df, names="scientific_domain", values="count", hole=0.55)
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader(tr("recent_vectors"))

display_df = df[["verified_at", "verdict", "score", "scientific_domain", "title", "statement"]].rename(
    columns={
        "verified_at": tr("verified_at"),
        "verdict": tr("verdict"),
        "score": tr("reliability_index"),
        "scientific_domain": tr("domain"),
        "title": tr("title"),
        "statement": tr("claim"),
    }
)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
)