import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_response(user_message):
    response = co.chat(
        model="command-a-03-2025",
        message=user_message
    )
    return response.text