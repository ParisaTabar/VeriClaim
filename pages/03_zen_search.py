import html
import os
import time
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd
import plotly.express as px
import psycopg2
import requests
import streamlit as st
from i18n import LANGUAGE_OPTIONS, tr, is_rtl

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "http://n8n:5678/webhook/verify-claim")
MODEL_NAME = os.getenv("VERICLAIM_MODEL_NAME", "llama-3.1-8b-instant")

DB_CONFIG: Dict[str, Any] = {
    "host": os.getenv("POSTGRES_HOST", "db"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "database": os.getenv("POSTGRES_DB", "vericlaim_db"),
    "user": os.getenv("POSTGRES_USER", "vericlaim_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "vericlaim_pass"),
}


def initialize_search_context() -> None:
    defaults: Dict[str, Any] = {
        "search_submitted": False,
        "current_query": "",
        "trigger_skeleton": False,
        "user_tier": st.session_state.get("user_tier", "Principal Investigator"),
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


@st.cache_data(ttl=20, show_spinner=False)
def execute_sovereign_query(query_string: str) -> pd.DataFrame:
    words = [w.strip() for w in query_string.strip().split() if len(w.strip()) > 2]
    if not words:
        return pd.DataFrame()

    conditions: List[str] = []
    params: List[Any] = []

    for word in words:
        like = f"%{word}%"
        conditions.append(
            "(" 
            "title ILIKE %s OR "
            "statement ILIKE %s OR "
            "verdict_summary ILIKE %s OR "
            "COALESCE(abstract, '') ILIKE %s OR "
            "COALESCE(keywords, '') ILIKE %s"
            ")"
        )
        params.extend([like, like, like, like, like])

    where_clause = " OR ".join(conditions)

    sql = f"""
        SELECT
            article_id,
            title,
            COALESCE(publication_year, EXTRACT(YEAR FROM CURRENT_DATE)::INT) AS publication_year,
            COALESCE(scientific_domain, 'General Sciences') AS scientific_domain,
            COALESCE(citations_count, 0) AS citations_count,
            canonical_url,
            doi,
            statement,
            category,
            extraction_model,
            COALESCE(certainty, 0.0) AS certainty,
            verdict,
            COALESCE(score, 0) AS score,
            verdict_summary,
            execution_time_ms,
            verified_at
        FROM sovereign_pipeline.latest_verifications
        WHERE {where_clause}
        ORDER BY score DESC, citations_count DESC, verified_at DESC
        LIMIT 25;
    """

    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            df = pd.read_sql_query(sql, conn, params=tuple(params))
            if not df.empty:
                df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
                df["certainty"] = pd.to_numeric(df["certainty"], errors="coerce").fillna(0.0)
                df["citations_count"] = pd.to_numeric(df["citations_count"], errors="coerce").fillna(0).astype(int)
            return df
    except Exception as err:
        st.error(f"RDM subsystem error: {err}")
        return pd.DataFrame()


def trigger_inference_pipeline(claim_query: str) -> bool:
    try:
        response = requests.post(N8N_WEBHOOK_URL, json={"claim": claim_query}, timeout=120)
        if response.status_code < 200 or response.status_code >= 300:
            st.error(f"n8n returned HTTP {response.status_code}: {response.text[:800]}")
            return False
        return True
    except requests.exceptions.Timeout:
        st.error("Pipeline timeout: the n8n inference graph exceeded the 120 second limit.")
        return False
    except requests.exceptions.RequestException as err:
        st.error(f"Gateway fault: cannot reach n8n orchestrator at {N8N_WEBHOOK_URL}. Details: {err}")
        return False


def render_system_status_bar() -> None:
    st.markdown(
        f"""
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:2rem; padding-bottom:1rem; border-bottom:1px solid rgba(51,65,85,0.4);">
            <span style="font-size:0.85rem; color:#94A3B8; letter-spacing:0.05em; text-transform:uppercase;">
                Infrastructure: <span style="color:#10B981;">Online</span>
                &nbsp;|&nbsp; Mode: <span style="color:#0EA5E9; font-weight:600;">Academic DSS</span>
            </span>
            <span style="background:rgba(14,165,233,0.1); color:#0EA5E9; border:1px solid rgba(14,165,233,0.3); padding:4px 12px; border-radius:12px; font-size:0.75rem; font-family:monospace;">
                MODEL: {html.escape(MODEL_NAME)}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_skeleton_loader() -> None:
    if not st.session_state.get("trigger_skeleton", False):
        return

    placeholder = st.empty()
    with placeholder.container():
        st.markdown(
            """
            <div class="vc-card" style="padding:2rem; margin-bottom:1rem; opacity:0.75;">
                <div style="width:20%; height:22px; background:rgba(14,165,233,0.25); border-radius:12px; margin-bottom:16px; animation:pulse 1.5s infinite;"></div>
                <div style="width:85%; height:18px; background:rgba(148,163,184,0.25); border-radius:8px; margin-bottom:10px; animation:pulse 1.5s infinite;"></div>
                <div style="width:60%; height:16px; background:rgba(148,163,184,0.18); border-radius:8px; margin-bottom:22px; animation:pulse 1.5s infinite;"></div>
                <div style="width:100%; height:6px; background:rgba(51,65,85,0.5); border-radius:4px; animation:pulse 1.5s infinite;"></div>
            </div>
            <style>
            @keyframes pulse { 0% { opacity:0.65; } 50% { opacity:0.25; } 100% { opacity:0.65; } }
            </style>
            """,
            unsafe_allow_html=True,
        )
    time.sleep(0.8)
    placeholder.empty()
    st.session_state.trigger_skeleton = False


def render_inline_analytics(df: pd.DataFrame) -> None:
    st.markdown(f"#### {tr('epistemic_overview')}")
    col1, col2, col3 = st.columns([1.2, 1, 1])

    with col1:
        fig = px.pie(
            df,
            names="verdict",
            hole=0.6,
            color="verdict",
            color_discrete_map={
                "supported": "#10B981",
                "mixed": "#F59E0B",
                "refuted": "#E11D48",
                "insufficient_evidence": "#64748B",
            },
        )
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(t=10, b=10, l=10, r=10),
            legend=dict(orientation="h", y=-0.15, x=0.5, xanchor="center"),
        )
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    with col2:
        st.metric(tr("mean_reliability"), f"{int(df['score'].mean())}%")
        st.metric(tr("evidence_vectors"), f"{len(df):,}")

    with col3:
        st.metric(tr("mean_certainty"), f"{float(df['certainty'].mean()):.2f} / 1.00")
        st.metric(tr("aggregated_citations"), f"{int(df['citations_count'].sum()):,}")


def verdict_style(verdict: str) -> Dict[str, str]:
    verdict = verdict.lower()
    if verdict == "supported":
        return {"label": tr("supported"), "color": "#10B981", "bg": "rgba(16,185,129,0.10)"}
    if verdict == "mixed":
        return {"label": tr("mixed"), "color": "#F59E0B", "bg": "rgba(245,158,11,0.10)"}
    if verdict == "refuted":
        return {"label": tr("refuted"), "color": "#E11D48", "bg": "rgba(225,29,72,0.10)"}
    return {"label": tr("insufficient_evidence"), "color": "#64748B", "bg": "rgba(100,116,139,0.10)"}


def render_result_cards(df: pd.DataFrame) -> None:
    st.markdown(f"**{tr('found_vectors', count=len(df))}**")
    for _, row in df.iterrows():
        style = verdict_style(str(row.get("verdict", "insufficient_evidence")))
        title = html.escape(str(row.get("title", "Untitled")))
        statement = html.escape(str(row.get("statement", "N/A")))
        summary = html.escape(str(row.get("verdict_summary", "No summary available.")))
        domain = html.escape(str(row.get("scientific_domain", "General Sciences")))
        url = html.escape(str(row.get("canonical_url") or row.get("doi") or "#"))
        score = int(row.get("score", 0))

        citations_label = tr("citations")
        year_label = tr("year")
        extracted_claim_label = tr("extracted_claim")
        model_rationale_label = tr("model_rationale")
        reliability_label = tr("reliability_index")
        source_label = tr("source")

        st.markdown(
            f"""
            <div class="vc-card" style="padding:1.6rem; margin:1rem 0;">
                <div style="display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; margin-bottom:12px;">
                    <span style="background:{style['bg']}; color:{style['color']}; border:1px solid {style['color']}; padding:4px 14px; border-radius:20px; font-size:0.78rem; font-weight:700; text-transform:uppercase; letter-spacing:0.04em;">
                        {style['label']}
                    </span>
                    <span style="color:#64748B; font-size:0.85rem; font-family:monospace;">
                        {domain} | {citations_label}: {int(row.get('citations_count', 0))} | {year_label}: {int(row.get('publication_year', datetime.now().year))}
                    </span>
                </div>
                <div style=" font-size:1.15rem; font-weight:650; line-height:1.42; margin-bottom:10px;">{title}</div>
                <div style=" font-size:0.95rem; line-height:1.55; margin-bottom:10px;">
                    <strong>{extracted_claim_label}:</strong> {statement}
                </div>
                <div style=" font-size:0.95rem; line-height:1.55; background:rgba(2,6,23,0.35); padding:14px; border-radius:10px; border-left:3px solid {style['color']};">
                    <strong style="color:#E2E8F0;">{model_rationale_label}:</strong> {summary}
                </div>
                <div style="margin-top:18px; display:flex; align-items:center; justify-content:space-between; gap:16px;">
                    <div style="width:72%;">
                        <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#64748B; margin-bottom:6px;">
                            <span>{reliability_label}</span><span style="color:#F1F5F9; font-weight:700;">{score}%</span>
                        </div>
                        <div style="background:rgba(51,65,85,0.5); height:7px; border-radius:4px; width:100%; overflow:hidden;">
                            <div style="width:{score}%; background:{style['color']}; height:100%;"></div>
                        </div>
                    </div>
                    <a href="{url}" target="_blank" style="color:#0EA5E9; text-decoration:none; font-size:0.85rem; font-weight:700; background:rgba(14,165,233,0.1); padding:8px 14px; border-radius:8px; border:1px solid rgba(14,165,233,0.3);">
                        {source_label}
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_zen_search_view() -> None:
    st.markdown("<div style='height:10vh;'></div>", unsafe_allow_html=True)
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown(
            f"""
            <div style="text-align:center; margin-bottom:2rem;">
                <h1 style="font-size:2.7rem; letter-spacing:-0.03em;">{tr("research_title")}</h1>
                <p style="color:#94A3B8; font-size:1.05rem;">
                    {tr("research_subtitle")}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.form("zen_search_form", clear_on_submit=False):
            user_input = st.text_input(
                tr("scientific_claim"),
                label_visibility="collapsed",
                placeholder=tr("claim_placeholder"),
                key="zen_input",
            )
            submitted = st.form_submit_button(tr("initiate_verification"), use_container_width=True, type="primary")

        if submitted and user_input.strip():
            st.session_state.current_query = user_input.strip()
            st.session_state.search_submitted = True
            st.session_state.trigger_skeleton = True
            st.rerun()


def render_workspace_view() -> None:
    st.markdown(f"### {tr('active_workspace')}")

    with st.form("inline_search", clear_on_submit=False):
        q_col, b_col = st.columns([4, 1])
        with q_col:
            new_input = st.text_input(
                tr("refine_query"),
                value=st.session_state.current_query,
                label_visibility="collapsed",
            )
        with b_col:
            submitted = st.form_submit_button(tr("reevaluate"), use_container_width=True)
        if submitted and new_input.strip():
            st.session_state.current_query = new_input.strip()
            st.session_state.trigger_skeleton = True
            execute_sovereign_query.clear()
            st.rerun()

    render_skeleton_loader()

    results_df = execute_sovereign_query(st.session_state.current_query)

    if results_df.empty:
        st.info(tr("no_local_evidence", query=st.session_state.current_query))
        with st.spinner(tr("pipeline_progress")):
            success = trigger_inference_pipeline(st.session_state.current_query)
        if success:
            st.success(tr("pipeline_completed"))
            execute_sovereign_query.clear()
            time.sleep(1.5)
            results_df = execute_sovereign_query(st.session_state.current_query)
        else:
            st.error(tr("pipeline_failed"))

    if not results_df.empty:
        render_inline_analytics(results_df)
        render_result_cards(results_df)
    else:
        st.warning(tr("no_vectors_persisted"))

    if st.button(tr("reset_workspace"), type="secondary"):
        st.session_state.search_submitted = False
        st.session_state.current_query = ""
        st.session_state.trigger_skeleton = False
        st.rerun()


def main() -> None:
    initialize_search_context()
    render_system_status_bar()
    if not st.session_state.search_submitted:
        render_zen_search_view()
    else:
        render_workspace_view()


if __name__ == "__main__":
    main()
