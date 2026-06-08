import streamlit as st
from i18n import LANGUAGE_OPTIONS, tr, is_rtl
from typing import List, Dict

# ==========================================
# 1. HOLOGRAPHIC STYLING ENGINE (LIQUID GLASS)
# ==========================================

def inject_responsive_css() -> None:
    """
    Injects hardware-accelerated CSS matrices for the landing node.
    Implements 'Liquid Glass' telemetry visuals, neon-glowing typography, 
    and adaptive flexbox containers. Strictly maintains the Sovereign AI aesthetic.
    """
    css = """
    <style>
    /* Responsive Hero Container & Kinetic Alignment */
    .hero-container { 
        display: flex;
        text-align: center;
        padding: clamp(3rem, 6vw, 5rem) 1rem 2rem 1rem;
        flex-direction: column;
        flex-wrap: nowrap;
        align-items: center;
        justify-content: center;
        animation: fade-in-up 0.8s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
    }
    
    /* Neon-Accented Fluid Typography */
    .hero-title { 
        font-size: clamp(2.2rem, 5vw, 4rem); 
        font-weight: 700; 
        color: #F1F5F9; 
        letter-spacing: -0.03em; 
        margin-bottom: 1.5rem;
        line-height: 1.15;
        text-shadow: 0 0 30px rgba(0, 240, 255, 0.15);
    }
    
    .hero-subtitle { 
        font-size: clamp(1rem, 2vw, 1.25rem); 
        color: #94A3B8; 
        max-width: 800px; 
        margin: 0 auto 3rem auto; 
        line-height: 1.7;
        font-weight: 400;
    }
    
    /* 3D Tactile Logo Node */
    .logo-container { 
        display: flex; 
        justify-content: center; 
        align-items: center; 
        margin-bottom: 24px; 
    }
    
    .logo-box { 
        background: rgba(14, 165, 233, 0.15); 
        color: #0EA5E9; 
        width: 64px; 
        height: 64px; 
        display: flex; 
        justify-content: center; 
        align-items: center; 
        border-radius: 16px; 
        font-weight: 700; 
        font-size: 28px; 
        border: 1px solid rgba(0, 240, 255, 0.4);
        box-shadow: 0 0 25px rgba(0, 240, 255, 0.2), inset 0 0 15px rgba(0, 240, 255, 0.1);
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.5);
    }
    
    /* Neumorphic Liquid Glass Feature Cards */
    .feature-card { 
        background: rgba(12, 18, 34, 0.5); 
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 240, 255, 0.15); 
        padding: 2.2rem; 
        border-radius: 18px; 
        text-align: left; 
        height: 100%;
        display: flex;
        flex-direction: column;
        box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.05), inset 0 1px 0 0 rgba(255, 255, 255, 0.05);
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    
    /* Cyberpunk Glow Hover State */
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(0, 240, 255, 0.15), inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
        border-color: rgba(0, 240, 255, 0.5);
    }
    
    .feature-title { 
        color: #0EA5E9; 
        font-weight: 600; 
        font-size: 1.15rem; 
        margin-bottom: 0.75rem; 
        letter-spacing: 0.02em;
    }
    
    .feature-text { 
        color: #94A3B8; 
        font-size: 0.95rem; 
        line-height: 1.6;
        flex-grow: 1; 
    }

    /* Subtle Entry Animation */
    @keyframes fade-in-up {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ==========================================
# 2. STRUCTURAL NODE RENDERING
# ==========================================

def render_hero_section() -> None:
    """
    Constructs the primary viewport presentation layer.
    Focuses the academic user on the core epistemic value proposition.
    """
    hero_html = f"""
    <div class="hero-container">
        <div class="logo-container">
            <div class="logo-box">VC</div>
        </div>
        <h1 class="hero-title">
            {tr("hero_title_line_1")} <br>
            <span style="color: #0EA5E9; text-shadow: 0 0 20px rgba(14,165,233,0.4);">
                {tr("hero_title_highlight")}
            </span>
        </h1>
        <p class="hero-subtitle">
            {tr("hero_subtitle")}
        </p>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)