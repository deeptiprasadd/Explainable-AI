import streamlit as st
import pandas as pd

st.title("Decision History Log")

try:
    log_df = pd.read_csv("decision_log.csv")
    st.dataframe(log_df)
except FileNotFoundError:
    st.info("No decisions recorded yet.")
