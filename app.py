import os
from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_response
from logger import log_conversation

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main chatbot web interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Processes user messages via POST and returns rule-based JSON bot responses."""
    data = request.get_json() or {}
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify({'response': 'Please enter a valid message.'})

    bot_response = get_bot_response(user_message)
    
    log_conversation(user_message, bot_response)

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    if not os.path.exists("logs"):
        os.makedirs("logs")
    app.run(host='127.0.0.1', port=5000, debug=True)
