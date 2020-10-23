from flask import Flask
from flask import request, jsonify
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


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        r = request.get_json()
        chat_id = r["message"]["chat"]["id"]
        message = r["message"]["text"]

        if "ethereum" in message:
            send_message(chat_id, text="some text")
        return jsonify(r)
    return "<h1>some text</h1>"


def main():
    pass


if __name__ == "__main__":
    app.run(debug=True)