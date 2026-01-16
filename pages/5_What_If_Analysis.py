import streamlit as st

st.title("What-if Analysis")

st.markdown("""
This tool allows users to explore how small changes in input
could affect the model decision.
""")

credit_score = st.slider("Credit Score", 300, 850, 620)
loan_amount = st.slider("Loan Amount", 50000, 1000000, 400000)

st.subheader("Simulated Outcome")

if credit_score > 700 and loan_amount < 300000:
    st.success("Simulated Result: Lower Risk")
else:
    st.warning("Simulated Result: Higher Risk")

st.info("""
What-if analysis helps users understand **decision sensitivity**
and provides actionable guidance to applicants.
""")
