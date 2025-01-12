import streamlit as st

from user import get_authenticator


st.title("Register User")

authenticator = get_authenticator()

try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = (
        authenticator.register_user(roles=["viewer"])
    )
    if email_of_registered_user:
        st.success("User registered successfully")
except Exception as e:
    st.error(e)
