import streamlit as st
from qdrant_client import models

import datetime

from user import get_authenticator, load_model
from db import load_data, get_likes_dislikes, add_like, add_dislike

st.title("EventConnect")

load_data()

authenticator = get_authenticator()
authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()

    username = st.session_state["username"]
    likes_dislikes = get_likes_dislikes(username)

    query_filter = models.Filter(
        must=[
            models.FieldCondition(
                key="date",
                range=models.Range(gte=int(datetime.datetime.now().strftime("%Y%m%d"))),
            )
        ]
    )

    _, qdrant_client, _ = load_model()
    recomm = qdrant_client.recommend(
        collection_name="my_events",
        positive=likes_dislikes["likes"],
        negative=likes_dislikes["dislikes"],
        query_filter=query_filter,
    )

    for event in recomm:
        idx = event.id
        payload = event.payload
        for img in payload["images"]:
            st.image(eval(img))
        st.write(payload["description"])
        st.write(payload["date"])
        st.write(payload["time"])

        st.button("Like", key=f"Like{idx}", on_click=lambda: add_like(username, idx))
        st.button(
            "Dislike", key=f"Dislike{idx}", on_click=lambda: add_dislike(username, idx)
        )


elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
