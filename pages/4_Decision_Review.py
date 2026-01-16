import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Decision Review")

if "uploaded_data" not in st.session_state:
    st.warning("Please upload data first.")
    st.stop()

df = st.session_state["uploaded_data"]

index = st.selectbox("Select record", df.index)
record = df.loc[index]

st.subheader("Applicant Data")
st.json(record.to_dict())

model_prediction = "High Risk"
confidence = 0.78

st.subheader("Model Recommendation")
st.write(f"Prediction: {model_prediction}")
st.write(f"Confidence: {confidence}")

decision = st.radio(
    "Final Decision",
    ["Approve", "Reject", "Escalate"]
)

reason = st.text_area("Reviewer Justification (required)")

if st.button("Submit Decision"):
    if not reason.strip():
        st.error("Justification is mandatory.")
    else:
        log = {
            "Timestamp": datetime.now(),
            "Record_ID": index,
            "Prediction": model_prediction,
            "Decision": decision,
            "Justification": reason
        }

        log_df = pd.DataFrame([log])
        log_df.to_csv(
            "decision_log.csv",
            mode="a",
            header=not st.session_state.get("log_exists", False),
            index=False
        )

        st.session_state["log_exists"] = True
        st.success("Decision recorded.")

from shared.audit_utils import save_audit_record

if st.button("Save Decision to Audit Log"):
    if not reason.strip():
        st.error("Justification is required for audit purposes.")
    else:
        save_audit_record(
            "decision_log.csv",
            record.to_dict(),
            model_prediction,
            decision,
            reason
        )
        st.success("Decision saved to audit log.")

