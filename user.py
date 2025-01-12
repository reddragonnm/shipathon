import streamlit_authenticator as stauth
import streamlit as st

import json


@st.cache_data
def load_db():
    pass


def get_authenticator():
    authenticator = stauth.Authenticate("./config.yaml")
    return authenticator


def get_likes_dislikes():
    username = st.session_state["name"]
