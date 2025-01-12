import streamlit as st
from db import add_user

from user import get_authenticator

# Set the title of the page
st.title("Register User")

# Initialize the authenticator to manage user registration
authenticator = get_authenticator()

# Attempt to register a new user
try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = (
        authenticator.register_user(
            roles=["viewer"]
        )  # Assign "viewer" role to the user
    )

    # Check if registration was successful
    if email_of_registered_user:
        st.success("User registered successfully")  # Display success message
        add_user(username_of_registered_user)  # Add the registered user to the database

# Handle any exceptions that may occur during registration
except Exception as e:
    st.error(e)
