import streamlit as st
import streamlit_analytics


with streamlit_analytics.track():
	st.text_input("Paranthaman")
	st.selectbox("select your favorite", ["guvi","data","science"])
	st.button("click me")
