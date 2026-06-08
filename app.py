import os
from i18n import LANGUAGE_OPTIONS, tr, is_rtl
from typing import Any, Dict

import streamlit as st

PAGE_TITLE = "VeriClaim | Academic DSS"
FAVICON_PATH = "assets/favicon.png"
PAGE_ICON = FAVICON_PATH if os.path.exists(FAVICON_PATH) else "🔬"
DEFAULT_ROLE = "Principal Investigator"

UI_MATRICES: Dict[str, Dict[str, str]] = {
    "Dark": {
        "app_bg": "radial-gradient(circle at 50% 0%, #0d1326 0%, #02040a 100%)",
        "glass_surface": "rgba(12, 18, 34, 0.5)",
        "neon_border": "rgba(0, 240, 255, 0.15)",
        "glow_shadow": "0 8px 32px 0 rgba(0, 240, 255, 0.05), inset 0 1px 0 0 rgba(255, 255, 255, 0.05)",
        "text_main": "#4B4B4B",
        "text_dim": "#64748B",
        "sidebar_bg": "linear-gradient(180deg, rgba(8, 12, 23, 0.85) 0%, rgba(2, 4, 10, 0.95) 100%)",
        "accent": "#aee6ff",
        "accent_dim": "rgba(14, 165, 233, 0.3)",
        "dropdown_bg": "#0f172a",
        "btn_bg": "#aee6ff !important",
        "btn_border": "rgba(0, 240, 255, 0.4)",
        "btn_hover": "rgba(0, 240, 255, 0.25)",
        "input_bg": "rgba(2, 6, 23, 0.6)"
    },
    "Light": {
        "app_bg": "radial-gradient(circle at 50% 0%, #f1f5f9 0%, #e2e8f0 100%)",
        "glass_surface": "rgba(255, 255, 255, 0.6)",
        "neon_border": "rgba(14, 165, 233, 0.2)",
        "glow_shadow": "0 8px 32px 0 rgba(14, 165, 233, 0.05), inset 0 1px 0 0 rgba(255, 255, 255, 0.4)",
        "text_main": "#0F172A",
        "text_dim": "#475569",
        "sidebar_bg": "linear-gradient(180deg, rgba(248, 250, 252, 0.8) 0%, rgba(226, 232, 240, 0.9) 100%)",
        "accent": "#aee6ff",
        "accent_dim": "rgba(2, 132, 199, 0.3)",
        "dropdown_bg": "#ffffff",
        "btn_bg": "#aee6ff !important",
        "btn_border": "rgba(14, 165, 233, 0.4)",
        "btn_hover": "rgba(14, 165, 233, 0.25)",
        "input_bg": "rgba(255, 255, 255, 0.4)"
    },
}


def initialize_runtime_environment() -> None:
    if "env_loaded" not in st.session_state:
        st.session_state.update(
            {
                "env_loaded": True,
                "logged_in": True,
                "user_tier": DEFAULT_ROLE,
                "theme": "Light",
                "language": "English",
            }
        )


def deploy_css_engine() -> None:
    direction = "rtl" if is_rtl() else "ltr"
    text_align = "right" if is_rtl() else "left"
    matrix = UI_MATRICES[st.session_state.theme]
    
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
                /* Force sidebar to stay visible in the local academic demo */
        section[data-testid="stSidebar"] {{
            display: block !important;
            visibility: visible !important;
            min-width: 285px !important;
            width: 285px !important;
            max-width: 285px !important;
            transform: translateX(0) !important;
            background: {matrix["sidebar_bg"]} !important;
            backdrop-filter: blur(24px) saturate(180%);
            -webkit-backdrop-filter: blur(24px) saturate(180%);
            border-right: 1px solid {matrix["neon_border"]};
            z-index: 999 !important;
        }}

        section[data-testid="stSidebar"] > div {{
            width: 285px !important;
            min-width: 285px !important;
        }}

        /* Hide Streamlit sidebar collapse controls */
        [data-testid="collapsedControl"],
        [data-testid="stSidebarCollapsedControl"],
        button[kind="headerNoPadding"] {{
            display: none !important;
            visibility: hidden !important;
            pointer-events: none !important;
        }}

        /* Keep the main content shifted correctly beside the fixed-width sidebar */
        .main .block-container {{
            max-width: 100% !important;
            padding-left: 3rem !important;
            padding-right: 3rem !important;
        }}
        .stApp {{
            background: {matrix['app_bg']} !important;
            background-attachment: fixed;
            font-family: 'Inter', sans-serif;
            color: {matrix['text_main']} !important;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {matrix['text_main']} !important;
            letter-spacing: -0.03em;
        }}
        p, span, label, .stMarkdown {{ color: {matrix['text_dim']} !important; }}

   /* Holographic Sidebar Styling */
    section[data-testid="stSidebar"] {{
        background: {matrix["sidebar_bg"]} !important;
        backdrop-filter: blur(24px) saturate(180%);
        -webkit-backdrop-filter: blur(24px) saturate(180%);
        border-right: 1px solid {matrix["neon_border"]};
    }}

    /* Core Data Containers */
    div[data-testid="stMetricSimpleContainer"], .vc-card {{
        background: {matrix["glass_surface"]} !important;
        backdrop-filter: blur(16px);
        border: 1px solid {matrix["neon_border"]} !important;
        border-radius: 16px !important;
        box-shadow: {matrix["glow_shadow"]} !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }}

    /* --- FORM OVERRIDES (BUTTONS, INPUTS, SELECTBOXES) --- */
    
    /* 1. Primary Buttons Override (Removing the Red) */
    button[kind="primaryFormSubmit"], 
    button[kind="primary"],
    [data-testid="stFormSubmitButton"] button {{
        background-color: {matrix["btn_bg"]} !important;
        color: {matrix["text_main"]} !important;
        border: 1px solid {matrix["btn_border"]} !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }}
    
    button[kind="primaryFormSubmit"]:hover, 
    button[kind="primary"]:hover,
    [data-testid="stFormSubmitButton"] button:hover {{
        background-color: {matrix["btn_hover"]} !important;
        box-shadow: 0 0 15px {matrix["btn_border"]} !important;
        transform: translateY(-2px);
        color: {matrix["text_main"]} !important;
        border-color: {matrix["text_main"]} !important;
    }}

    /* 2. Secondary Buttons Override */
    button[kind="secondary"] {{
        background-color: transparent !important;
        border: 1px solid {matrix["text_dim"]} !important;
        color: {matrix["text_main"]} !important;
        border-radius: 8px !important;
    }}
    button[kind="secondary"]:hover {{
        border-color: {matrix["text_main"]} !important;
    }}

    /* 3. Input Fields & Dropdowns (Removing the White BaseWeb) */
    div[data-baseweb="input"], 
    div[data-baseweb="select"] > div,
    div[data-baseweb="base-input"] {{
        background-color: {matrix["input_bg"]} !important;
        border: 1px solid {matrix["neon_border"]} !important;
        border-radius: 8px !important;
        color: {matrix["text_main"]} !important;
    }}

    /* Input Text Color Fix */
    input, .stSelectbox span, div[data-baseweb="select"] div {{
        color: {matrix["text_main"]} !important;
    }}
    
    /* Dropdown Popover Menu Fix */
    ul[role="listbox"] {{
        background-color: {matrix["app_bg"]} !important;
        border: 1px solid {matrix["neon_border"]} !important;
    }}
    li[role="option"] {{
        color: {matrix["text_main"]} !important;
        
    }}
    li[role="option"]:hover {{
        background-color: {matrix["btn_bg"]} !important;
    }}
    
    span[data-baseweb="tag"] {{
        background-color: rgba(14, 165, 233, 0.2) !important;
    }}

    /* Correcting the CSS bracket syntax for Streamlit injection */
    .stApp {{
        background: {matrix["app_bg"]} !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: {matrix["text_main"]} !important;
    }}
    /* 1. Primary Button Styling - Using the matrix for colors */
    button[kind="primaryFormSubmit"] {{
        background-color: {matrix["accent"]} !important;
        color: #ffffff !important;
        border: 1px solid {matrix["neon_border"]} !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }}
    
    button[kind="primaryFormSubmit"]:hover {{
        background-color: transparent !important;
        border-color: {matrix["accent"]} !important;
        color: {matrix["accent"]} !important;
        box-shadow: 0 0 15px {matrix["accent_dim"]} !important;
    }}

    /* 2. Fixing the Dropdown (The white background issue) */
    div[data-baseweb="popover"] {{
        background-color: {matrix["dropdown_bg"]} !important;
        border: 1px solid {matrix["neon_border"]} !important;
    }}
    
    li[role="option"] {{
        background-color: {matrix["dropdown_bg"]} !important;
        color: {matrix["text_main"]} !important;
    }}
    
    li[role="option"]:hover {{
        background-color: {matrix["accent_dim"]} !important;
        color: {matrix["accent"]} !important;
    }}

    /* 3. Input fields background fix */
    div[data-baseweb="select"] > div {{
        background-color: {matrix["glass_surface"]} !important;
        color: {matrix["text_main"]} !important;
    }}
    
    /* Fix for multi-select tags */
    span[data-baseweb="tag"] {{
        background-color: {matrix["accent_dim"]} !important;
        color: {matrix["text_main"]} !important;
        border: 1px solid {matrix["neon_border"]} !important;
    }}
    /* Strip commercial visual clutter */
    #MainMenu, footer {{ display: none !important; }}
    header[data-testid="stHeader"] {{ background: transparent !important; }}
     
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.stDeployButton {{
    display: none !important;
    visibility: hidden !important;
}}

        /* Smaller academic-demo sidebar logo */
        .vc-sidebar-logo {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0.75rem auto 1.25rem auto;
        }}

        .vc-sidebar-logo img {{
            width: 150px;
            max-width: 70%;
            height: auto;
            opacity: 0.96;
        }}
        
        .stApp {{
    direction: {direction};
    text-align: {text_align};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_header() -> None:
    theme = st.session_state.get("theme", "Light")
    logo_path = f"assets/logo_{theme.lower()}.png"

    st.sidebar.markdown(
        """
        <div class="vc-sidebar-fixed-header">
            <div style="height:0.5rem;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if os.path.exists(logo_path):
        left, center, right = st.sidebar.columns([1.05, 1.9, 1.05])
        with center:
            st.image(logo_path, use_container_width=True)
    else:
        st.sidebar.markdown(
            f"""
            <div style="text-align:center; padding:0.5rem 0 1rem 0;">
                <h2 style="margin-bottom:0.25rem;">🔬 VeriClaim</h2>
                <div style="font-size:0.78rem; opacity:0.72;">
                    {tr("status_academic_dss")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.sidebar.divider()


def render_sidebar_footer() -> None:
    theme_opts = ["Dark", "Light"]
    current_theme = st.session_state.get("theme", "Light")
    current_theme_idx = theme_opts.index(current_theme) if current_theme in theme_opts else 1

    selected_theme = st.sidebar.selectbox(
        tr("display_matrix"),
        theme_opts,
        index=current_theme_idx,
        key="display_matrix_select",
    )

    if selected_theme != st.session_state.theme:
        st.session_state.theme = selected_theme
        st.rerun()

    lang_opts = list(LANGUAGE_OPTIONS.keys())
    current_lang = st.session_state.get("language", "English")
    current_lang_idx = lang_opts.index(current_lang) if current_lang in lang_opts else 0

    selected_lang = st.sidebar.selectbox(
        tr("system_language"),
        lang_opts,
        index=current_lang_idx,
        key="language_select",
    )

    if selected_lang != st.session_state.language:
        st.session_state.language = selected_lang
        st.rerun()

    st.sidebar.divider()
    st.sidebar.caption(tr("commercial_disabled_caption"))


def main() -> None:
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    initialize_runtime_environment()
    deploy_css_engine()

    render_sidebar_header()

    search_node = st.Page(
        "pages/03_zen_search.py",
        title=tr("nav_research_engine"),
        icon="🔍",
        url_path="research",
    )

    dashboard_node = st.Page(
        "pages/04_dashboard.py",
        title=tr("nav_system_telemetry"),
        icon="📊",
        url_path="dashboard",
    )

    methods_node = st.Page(
        "pages/05_methods.py",
        title=tr("nav_methods"),
        icon="📘",
        url_path="methods",
    )

    audit_node = st.Page(
        "pages/05_deep_audit.py",
        title=tr("nav_deep_audit"),
        icon="📑",
        url_path="audit",
    )

    vault_node = st.Page(
        "pages/06_vault.py",
        title=tr("nav_data_lineage_vault"),
        icon="🗄️",
        url_path="vault",
    )

    router = st.navigation(
        {
            tr("group_verification_workflow"): [search_node, dashboard_node],
            tr("group_research_governance"): [methods_node, audit_node, vault_node],
        }
    )

    render_sidebar_footer()

    router.run()


if __name__ == "__main__":
    main()