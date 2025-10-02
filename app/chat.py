# app/chat.py

from .api_client import GroqClient

class ChatManager:
    """Class to manage chat interactions."""

    def __init__(self):
        self.client = GroqClient()  # Initialize the Groq client
        self.conversation_history = []  # Store conversation history

    def add_message(self, role, content):
        """Add a message to the conversation history."""
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, user_message):
        """
        Get a concise or detailed response based on user input.

        :param user_message: The message input from the user.
        :return: AI response as a string.
        """
        # Add user's message to history
        self.add_message("user", user_message)

        # Prepare messages for the API call based on user intent
        if any(keyword in user_message.lower() for keyword in ["what is", "define"]):
            prompt = f"Provide a concise definition of: {user_message}"
        
        elif "explain" in user_message.lower() or "code" in user_message.lower():
            prompt = f"Explain clearly with examples: {user_message}"
        
        else:
            prompt = f"Respond concisely to: {user_message}"

        messages = [{"role": "user", "content": prompt}]

        # Get AI response
        ai_response = self.client.get_response(messages)

        # Add AI's response to history
        self.add_message("assistant", ai_response)

        return ai_response