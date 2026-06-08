import streamlit as st
from i18n import tr


st.title(tr("deep_audit_title"))
st.caption(tr("deep_audit_subtitle"))

step_1 = tr("deep_audit_step_1")
step_2 = tr("deep_audit_step_2")
step_3 = tr("deep_audit_step_3")
step_4 = tr("deep_audit_step_4")
step_5 = tr("deep_audit_step_5")

st.markdown(
    f"""
<p>{tr("deep_audit_stub")}</p>

<p><strong>{tr("planned_workflow")}</strong></p>

<ol>
    <li>{step_1}</li>
    <li>{step_2}</li>
    <li>{step_3}</li>
    <li>{step_4}</li>
    <li>{step_5}</li>
</ol>

<p>{tr("deep_audit_mvp_note")}</p>
""",
    unsafe_allow_html=True,
)

st.file_uploader(
    tr("upload_future"),
    type=["pdf", "csv"],
    disabled=True,
)

st.info(tr("batch_disabled"))