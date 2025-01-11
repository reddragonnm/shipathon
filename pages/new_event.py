import streamlit as st

st.title("New event")

image = st.file_uploader("Upload image")
text = st.text_area("Description")
date = st.date_input("Date of event")
time = st.time_input("Time of event")

button = st.button("Add event")
