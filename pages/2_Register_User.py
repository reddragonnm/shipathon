import streamlit as st

from user import get_authenticator


st.title("Register User")

authenticator = get_authenticator()
