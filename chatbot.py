import os
from dotenv import load_dotenv
import openai


load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  engine="davinci",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n", " Human:", " AI:"]
)

def ask(question, chat_log=None):
 prompt_text = f’{chat_log}{restart_sequence}: {question}{start_sequence}:’
 response = openai.Completion.create(
 engine=”davinci”,
 prompt=prompt_text,
 temperature=0.8,
 max_tokens=150,
 top_p=1,
 frequency_penalty=0,
 presence_penalty=0.3,
 stop=[“\n”],
 )
 story = response[‘choices’][0][‘text’]
 return str(story)
