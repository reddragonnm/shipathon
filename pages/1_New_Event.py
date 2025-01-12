import streamlit as st

from user import get_authenticator

st.title("Add new event")

authenticator = get_authenticator()

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()

    if "admin" in st.session_state["roles"]:

        st.title("New event")

        image = st.file_uploader("Upload image")
        text = st.text_area("Description")
        date = st.date_input("Date of event")
        time = st.time_input("Time of event")

        button = st.button("Add event")
    else:
        st.warning("You are not authorized for this action")

elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
