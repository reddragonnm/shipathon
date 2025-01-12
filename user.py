import streamlit_authenticator as stauth
import streamlit as st

import google.generativeai as genai
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer


def get_authenticator():
    # Initialize and return an authentication object.The function uses a configuration file to set up authentication for the application.

    authenticator = stauth.Authenticate("./config.yaml")
    return authenticator


@st.cache_resource
def load_model():
    # Configure the generative AI client using the API key stored in Streamlit secrets and initialize the generative AI model with the specified model type
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Create a Qdrant client for interacting with the vector database
    qdrant_client = QdrantClient(
        url="https://bd3982d8-a9af-40b3-b38c-7afb14f47da2.us-east-1-0.aws.cloud.qdrant.io:6333",
        api_key=st.secrets["QDRANT_CLOUD_API_KEY"],
    )

    # Initialize a sentence encoder for generating text embeddings
    encoder = SentenceTransformer("all-MiniLM-L6-v2")

    return model, qdrant_client, encoder
