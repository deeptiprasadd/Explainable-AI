import pandas as pd
from datetime import datetime

def save_audit_record(filename, record, prediction, decision, reason):
    audit_entry = {
        "Timestamp": datetime.now(),
        "Prediction": prediction,
        "Final Decision": decision,
        "Justification": reason,
        **record
    }

    df = pd.DataFrame([audit_entry])

    try:
        df.to_csv(filename, mode="a", header=False, index=False)
    except FileNotFoundError:
        df.to_csv(filename, index=False)

    return True
