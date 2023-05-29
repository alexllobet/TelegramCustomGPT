import requests
from dotenv import load_dotenv
import os

TOKEN = os.getenv("TOKEN")

def filter_textual_msg(message):
    if 'message' in message and 'text' in message['message']:
        return message
    else:
        return None
def handle_request(message):
    message = filter_textual_msg(message)
    if message is not None:
        chat_id, txt = parse_message(message)
        if txt == "hi":
            tel_send_message(chat_id, "Hello!!")
        else:
            tel_send_message(chat_id, 'from webhook')
            
def parse_message(message):
    # Discard updates with no message or message without content
    print("message-->", message)
    chat_id, txt = message['message']['chat']['id'], message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r