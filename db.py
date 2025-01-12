import streamlit as st
from google.cloud import firestore

DEFAULT = {"likes": [1], "dislikes": []}


@st.cache_resource
def get_db():
    db = firestore.Client.from_service_account_info(st.secrets["firebase"])
    return db


def add_user(username):
    # Add a new user to the database with default likes and dislikes.
    db = get_db()
    db.collection("users").document(username).set(DEFAULT)


def get_likes_dislikes(username):
    # Retrieve the likes and dislikes of a user. If the user does not exist, add them to the database.
    db = get_db()
    doc = db.collection("users").document(username).get()

    if not doc.exists:
        add_user(username)
        return DEFAULT

    return doc.to_dict()


def add_like(username, idx):
    # Add an event ID to the user's list of likes if it is not already present.
    db = get_db()
    doc_ref = db.collection("users").document(username)
    doc_ref.update({"likes": firestore.ArrayUnion([idx])})


def add_dislike(username, idx):
    # Add an event ID to the user's list of dislikes if it is not already present.
    db = get_db()
    doc_ref = db.collection("users").document(username)
    doc_ref.update({"dislikes": firestore.ArrayUnion([idx])})
