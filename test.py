import os

import google.generativeai as genai
from dotenv import load_dotenv

from qdrant_client import QdrantClient, models

load_dotenv()

# tags = ["dance", "music", "writing", "design", "other", "technical", ""]


# def load_model():
#     genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#     model = genai.GenerativeModel(
#         "gemini-1.5-flash",
#         system_instruction="For the given description and/or image give the tag",
#     )

#     return model


# model = load_model()

# text = ""

# response = model.generate_content(
#     text,
#     generation_config=genai.GenerationConfig(
#         response_mime_type="application/json",
#         response_schema={
#             "type": "object",
#             "properties": {
#                 "tag": {
#                     "type": "string",
#                     "enum": tags,
#                 },
#             },
#             "required": ["tag"],
#         },
#     ),
# )


qdrant_client = QdrantClient(
    url="https://bd3982d8-a9af-40b3-b38c-7afb14f47da2.us-east-1-0.aws.cloud.qdrant.io:6333",
    api_key=os.getenv("QDRANT_CLOUD_API_KEY"),
)

print(qdrant_client.get_collections())
