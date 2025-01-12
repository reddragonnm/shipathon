import os

import streamlit as st

from user import get_authenticator

st.title("EventConnect")

authenticator = get_authenticator()
authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()

    st.write("Hello world")

elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
