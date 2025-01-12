import streamlit as st
import base64

from qdrant_client import models

from user import get_authenticator, load_model


st.title("Add new event")

authenticator = get_authenticator()
authenticator.login()


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
            text = description
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

                text += " " + response.text

            next_id = (
                qdrant_client.count(
                    collection_name="my_events",
                    exact=True,
                ).count
                + 1
            )

            qdrant_client.upsert(
                collection_name="my_events",
                points=[
                    models.PointStruct(
                        id=next_id,
                        vector=encoder.encode(text).tolist(),
                        payload={
                            "date": int(date.strftime("%Y%m%d")),
                            "time": time,
                            "description": description,
                            "images": [str(image.getvalue()) for image in images],
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
