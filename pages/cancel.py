
import streamlit as st

st.title("Payment Cancelled")
st.warning("Your payment was cancelled. Please try again if you wish to complete your purchase.")
st.button("Return to Store", on_click=lambda: st.session_state.update({"page": "main"}))
