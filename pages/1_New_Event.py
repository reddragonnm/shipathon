import os
import streamlit as st
from dotenv import load_dotenv
import base64

import google.generativeai as genai
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

from user import get_authenticator

load_dotenv()

st.title("Add new event")

authenticator = get_authenticator()
authenticator.login()


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


if st.session_state["authentication_status"]:
    authenticator.logout()

    if "admin" in st.session_state["roles"]:

        st.title("New event")

        model, qdrant_client, encoder = load_model()

        images = st.file_uploader("Upload images", accept_multiple_files=True)
        description = st.text_area("Description")
        date = st.date_input("Date of event")
        time = st.time_input("Time of event")

        button = st.button("Add event")

        if button:
            if images is not None:
                response = model.generate_content(
                    [
                        *[
                            {
                                "mime_type": "image/jpeg",
                                "data": base64.b64encode(image.getvalue()).decode(
                                    "utf-8"
                                ),
                            }
                            for image in images
                        ],
                        "Extract all important data from all images. Don't add introduction. Get straight to the point.",
                    ]
                )

            st.write(description)

            qdrant_client.upload_points(
                collection_name="my_events",
                points=[
                    models.PointStruct(
                        vector=encoder.encode(
                            description + " " + response.text
                        ).tolist(),
                        payload={
                            "date": date,
                            "time": time,
                            "description": description,
                        },
                    )
                ],
            )

    else:
        st.warning("You are not authorized for this action")

elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
