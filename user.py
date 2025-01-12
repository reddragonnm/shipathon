import os
from dotenv import load_dotenv

load_dotenv()

import streamlit_authenticator as stauth
import streamlit as st

import google.generativeai as genai
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer


def get_authenticator():
    authenticator = stauth.Authenticate("./config.yaml")
    return authenticator


@st.cache_resource
def load_model():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")

    qdrant_client = QdrantClient(
        url="https://bd3982d8-a9af-40b3-b38c-7afb14f47da2.us-east-1-0.aws.cloud.qdrant.io:6333",
        api_key=os.getenv("QDRANT_CLOUD_API_KEY"),
    )

    encoder = SentenceTransformer("all-MiniLM-L6-v2")

    return model, qdrant_client, encoder
