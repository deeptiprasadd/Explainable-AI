import streamlit as st
import pandas as pd
import numpy as np

st.title("Model Comparison")

st.markdown("""
This section compares two commonly used models:
- Logistic Regression (interpretable baseline)
- Random Forest (non-linear ensemble)
""")

features = [
    "Credit Score", "Annual Income", "Loan Amount",
    "Age", "Existing Loans"
]

comparison = pd.DataFrame({
    "Feature": features,
    "Logistic Regression Importance": [0.42, 0.21, 0.18, 0.12, 0.07],
    "Random Forest Importance": [0.35, 0.28, 0.22, 0.10, 0.05]
}).set_index("Feature")

st.bar_chart(comparison)

st.info("""
Differences in importance indicate how model complexity
changes decision reasoning.
""")
