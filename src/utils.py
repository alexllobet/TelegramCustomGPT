import requests
from dotenv import load_dotenv
import os

TOKEN = os.getenv("TOKEN")



def parse_message(message):
    # Discard updates with no message or message without content
    if 'message' not in message:
        return -1, -1
    elif 'text' not in message['message']:
        return -1 ,-1
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