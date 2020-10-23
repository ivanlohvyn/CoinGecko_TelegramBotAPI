from flask import Flask
from flask_sslify import SSLify
import requests
import json


app = Flask(__name__)
sslify = SSLify(app)

URL = "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/"


def write_json(data, filename="bot_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_updates():
    url = URL + "getUpdates"
    r = requests.get(url)
    write_json(r.json())


def send_message(chat_id, text="some text"):
    url = URL + "sendMessage"
    answer = {"chat_id": chat_id, "text": text}
    r = requests.post(url, json=bot_data)
    return r.json


def main():
    get_updates()
    chat = r["message"]["chat"][id]
    send_message(chat_id)


if __name__ == "__main__":
    main()