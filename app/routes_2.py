from flask import Blueprint, render_template, request, jsonify
from .utils import format_response
from .chat import ChatManager

main = Blueprint('main', __name__)

chat_manager = ChatManager()

@main.route('/')
def index():
    return render_template('chat.html')

@main.route('/api/chat', methods=['POST'])
def chat():

    user_message = request.json.get('message')

    if not user_message:
        return jsonify({"error":"No Message Provided"}, 400)
    ai_response = chat_manager.get_response(user_message)

    formatted_response = format_response(ai_response)

    return jsonify({"response":formatted_response})
