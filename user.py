import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader


class User:
    def __init__(self, username):
        self.username = username
        self.likes = []
        self.dislikes = []

        self.clubs_subscribed = []

    def get_data(self):
        data = {"likes": self.likes, "dislikes": self.dislikes}
        return data


def get_authenticator():
    with open("./config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )

    return authenticator
