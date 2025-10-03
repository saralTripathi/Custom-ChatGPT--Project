# app/api_client.py

import os
from groq import Groq 
from dotenv import load_dotenv
load_dotenv()

class GroqClient:

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.client = Groq(api_key=self.api_key)

    def get_response(self, message):
        chat_completion = self.client.chat.completions.create(
            messages=message,
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )

        response = chat_completion.choices[0].message.content
        return response
