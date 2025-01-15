
import streamlit as st

st.title("Payment Successful!")
st.balloons()
st.success("Thank you for your purchase!")
st.button("Return to Store", on_click=lambda: st.session_state.update({"page": "main"}))
