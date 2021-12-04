import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''


def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'

>>> from chatbot import ask, append_interaction_to_chat_log
>>> chat_log = None

>>> question = 'Who played Forrest Gump in the movie?'
>>> answer = ask(question, chat_log)
>>> answer
'Forrest Gump is a 1994 American romantic comedy-drama film based on the 1986 novel of the same name by Winston Groom. The film was directed by Robert Zemeckis and was adapted for the screen by Eric Roth. It stars Tom Hanks as Forrest Gump, for which he won the Academy Award for Best Actor, and was nominated for Best Picture.'

>>> chat_log = append_interaction_to_chat_log(question, answer, chat_log)

>>> question = 'Was he in any other great roles?'
>>> answer = ask(question, chat_log)
>>> answer
'He played the protagonist in The Green Mile (1999), a drama film based on the Stephen King novel of the same name.'
