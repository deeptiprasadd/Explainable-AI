import streamlit as st

st.title("Ethics, Limitations, and Responsible Use")

st.markdown("""
### Limitations
- Feature importance does not imply causality
- Correlated variables may distort explanations
- Models may reflect historical bias

### Ethical Considerations
- Automated decisions must be explainable
- Users have the right to understand outcomes
- Human review is mandatory in high-impact cases

### Responsible AI Principle
Machine learning should **support** decision-makers,
not replace them.
""")

st.success("This system prioritizes transparency and accountability.")
