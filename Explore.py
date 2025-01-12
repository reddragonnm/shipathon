import streamlit as st
from qdrant_client import models
import datetime

# Import custom functions and utilities
from user import get_authenticator, load_model
from db import get_likes_dislikes, add_like, add_dislike

# Set the title of the Streamlit app
st.title("EventConnect")

# Initialize the authenticator and log in the user
authenticator = get_authenticator()
authenticator.login()

# Check if the user is authenticated
if st.session_state["authentication_status"]:
    # Make logout button
    authenticator.logout()

    # Retrieve the authenticated user's username
    username = st.session_state["username"]

    # Get the user's liked and disliked events
    likes_dislikes = get_likes_dislikes(username)

    # Define a query filter for recommending events happening today or in the future
    query_filter = models.Filter(
        must=[
            models.FieldCondition(
                key="date",  # Field to filter on
                range=models.Range(
                    gte=int(datetime.datetime.now().strftime("%Y%m%d"))
                ),  # Events on or after today's date
            )
        ]
    )

    # Load the generative model and Qdrant client
    _, qdrant_client, _ = load_model()

    # Get event recommendations based on the user's likes and dislikes
    recomm = qdrant_client.recommend(
        collection_name="my_events",
        positive=likes_dislikes["likes"],  # Positive preferences
        negative=likes_dislikes["dislikes"],  # Negative preferences
        query_filter=query_filter,  # Apply the date filter
    )

    # Display the recommended events
    for event in recomm:
        idx = event.id
        payload = event.payload

        for img in payload["images"]:
            st.image(eval(img))  # Use eval to parse the image URL

        # Display event details
        st.write(payload["description"])
        st.write(payload["date"])
        st.write(payload["time"])

        # Add Like and Dislike buttons with their respective actions
        st.button("Like", key=f"Like{idx}", on_click=lambda: add_like(username, idx))
        st.button(
            "Dislike", key=f"Dislike{idx}", on_click=lambda: add_dislike(username, idx)
        )

        st.divider()

# Handle authentication failures
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")  # Show an error message if login fails
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")  # Prompt the user to log in
