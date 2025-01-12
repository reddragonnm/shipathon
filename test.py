import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

tags = ["dance", "music", "writing", "design", "other", "technical", ""]


def load_model():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction="For the given description and/or image give the tag",
    )

    return model


model = load_model()

text = ""

response = model.generate_content(
    text,
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema={
            "type": "object",
            "properties": {
                "tag": {
                    "type": "string",
                    "enum": tags,
                },
            },
            "required": ["tag"],
        },
    ),
)
