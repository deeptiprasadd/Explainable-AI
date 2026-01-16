import streamlit as st

st.set_page_config(
    page_title="Explainable AI Dashboard",
    layout="wide"
)

st.title("Explainable AI Dashboard")
st.subheader("Credit Risk & Decision Transparency")

st.markdown("""
This application demonstrates how **machine learning decisions can be explained**
and audited in high-stakes financial systems.

Use the navigation menu on the left to explore:
- Model performance metrics
- Feature importance
- Decision explanations
- Ethical considerations
""")

st.info("""
This system is designed for **decision transparency**, not automated approval.
Human oversight is always required.
""")
