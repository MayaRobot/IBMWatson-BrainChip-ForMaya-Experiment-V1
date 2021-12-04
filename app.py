from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import ask, append_interaction_to_chat_log

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
