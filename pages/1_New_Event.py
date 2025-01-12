import streamlit as st
import base64

from qdrant_client import models

from user import get_authenticator, load_model


st.title("Add new event")

# Initialize the authenticator for user authentication
authenticator = get_authenticator()
authenticator.login()

# Check if the user is authenticated
if st.session_state["authentication_status"]:
    authenticator.logout()

    # Check if the authenticated user has the "admin" role
    if "admin" in st.session_state["roles"]:
        # Load the generative model, Qdrant client, and encoder
        model, qdrant_client, encoder = load_model()

        # Input fields for the event
        images = st.file_uploader(
            "Upload images", accept_multiple_files=True
        )  # Upload multiple images
        description = st.text_area("Description")  # Add event description
        date = st.date_input("Date of event")  # Select event date
        time = st.time_input("Time of event")  # Select event time

        # Button to add the event
        button = st.button("Add event")

        # Logic to handle event submission
        if button:
            model_output = ""

            # If images are uploaded, process them using the generative model
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
                        # Instruction for the model to extract meaningful data from the images
                        "Extract all important data from all images. Don't add introduction. Get straight to the point.",
                    ]
                )

                model_output = response.text

            # Calculate the next unique ID for the new event
            next_id = (
                qdrant_client.count(
                    collection_name="my_events",
                    exact=True,
                ).count
                + 1
            )

            # Insert the new event into the Qdrant vector database
            qdrant_client.upsert(
                collection_name="my_events",
                points=[
                    models.PointStruct(
                        id=next_id,
                        vector=encoder.encode(
                            description + " " + model_output
                        ).tolist(),  # Vector representation of the event text
                        payload={
                            "date": int(
                                date.strftime("%Y%m%d")
                            ),  # Event date in YYYYMMDD format
                            "time": time,
                            "description": description,
                            "images": [
                                str(image.getvalue()) for image in images
                            ],  # Raw image data
                            "model_output": model_output,
                        },
                    )
                ],
            )

            # Display success message
            st.success("Event added successfully!")

    else:
        # Warn the user if they are not authorized to add events
        st.warning("You are not authorized for this action")

# Handle cases where authentication fails
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
