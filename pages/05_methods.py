import streamlit as st
from i18n import tr


st.title(tr("methods_title"))
st.caption(tr("methods_subtitle"))

st.markdown(
    f"""
### {tr("methodological_positioning")}

{tr("methods_positioning_body")}

{tr("methods_pipeline_intro")}

1. **{tr("methods_claim_intake_title")}**: {tr("methods_claim_intake_body")}
2. **{tr("methods_query_compression_title")}**: {tr("methods_query_compression_body")}
3. **{tr("methods_evidence_retrieval_title")}**: {tr("methods_evidence_retrieval_body")}
4. **{tr("methods_evidence_scoring_title")}**: {tr("methods_evidence_scoring_body")}

### {tr("reliability_index_section")}

{tr("methods_reliability_body")}

### {tr("verdict_taxonomy")}

- **supported**: {tr("methods_supported_definition")}
- **mixed**: {tr("methods_mixed_definition")}
- **refuted**: {tr("methods_refuted_definition")}
- **insufficient_evidence**: {tr("methods_insufficient_definition")}

### {tr("known_limitations")}

- {tr("methods_limitation_abstract")}
- {tr("methods_limitation_citations")}
- {tr("methods_limitation_llm")}
- {tr("methods_limitation_sources")}
- {tr("methods_limitation_consensus")}

### {tr("intended_use")}

{tr("methods_intended_use_body")}
"""
)

st.info(tr("methods_demo_framing"))