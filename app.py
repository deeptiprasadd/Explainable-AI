import streamlit as st

# --------------------------------------------------
# App Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Explainable AI Decision Review System",
    layout="wide"
)

# --------------------------------------------------
# Landing Page (Home)
# --------------------------------------------------
st.title("Explainable AI Decision Review System")

st.markdown("""
### Purpose of This Application

This application is a **multi-page Explainable AI (XAI) platform**
designed to support **transparent, auditable, and human-centered
decision making** in high-stakes domains.

The system allows users to:
- Upload and analyze real-world data
- Review machine learning recommendations
- Understand feature-level explanations
- Make final human decisions
- Maintain an audit trail for compliance

This project demonstrates how **AI systems should assist humans,
not replace them**.
""")

st.markdown("""
### How to Use the Dashboard

Use the navigation panel on the left to explore:

- **Dashboard** — System-level metrics and trends  
- **Data Overview** — Upload and inspect real user data  
- **Model Comparison** — Compare how different models reason  
- **Decision Review** — Approve, reject, or escalate cases  
- **What-if Analysis** — Explore how changes affect outcomes  
- **Decision History** — Review past decisions for audit  
- **Ethics & Limitations** — Understand responsible AI boundaries
""")

st.info("""
This system is intentionally designed with **human-in-the-loop control**.
Automated recommendations should always be reviewed by a qualified user.
""")
