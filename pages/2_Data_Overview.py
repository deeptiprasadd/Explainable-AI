import streamlit as st
import pandas as pd

st.title("Data Upload & Overview")

st.markdown("""
Upload a CSV file containing applicant data.
Each row will be treated as a separate decision case.
""")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["uploaded_data"] = df
    st.success("Data uploaded successfully.")
    st.dataframe(df.head())
else:
    st.info("Awaiting CSV upload.")

st.markdown("""
Required columns (example):
- Age
- Annual_Income
- Credit_Score
- Loan_Amount
- Existing_Loans
""")
