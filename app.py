from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import ask, append_interaction_to_chat_log

app = Flask(__name__)


@app.route('/chatbot', methods=['POST'])
def chatbot():
    incoming_msg = request.values['Body']

    # use the incoming message to generate the response here

    r = MessagingResponse()
    r.message('this is the response')
    return str(r)
