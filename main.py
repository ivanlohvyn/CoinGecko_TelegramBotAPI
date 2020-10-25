import json
import re

import requests
from flask import Flask, jsonify, request
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)


URL = "https://api.telegram.org/bot<token>/"


def write_json(data, filename="bot_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def get_updates():
    url = URL + "getUpdates"
    r = requests.get(url)
    write_json(r.json())


def send_message(chat_id, text="some text"):
    url = URL + "sendMessage"
    response = {"chat_id": chat_id, "text": text}
    r = requests.post(url, json=response)
    return r.json


def parse_text(text):
    pattern = r"=\w+"
    crypto = re.search(pattern, text).group()
    return crypto[1:]


def get_price(crypto):
    url = (
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={}".format(
            crypto
        )
    )
    r = requests.get(url).json()
    price = r[-1]["current_price"]
    return price


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        r = request.get_json()
        chat_id = r["message"]["chat"]["id"]
        message = r["message"]["text"]

        pattern = r"=\w+"

        if re.search(pattern, message):
            price = get_price(parse_text(message))
            send_message(chat_id, text=price)
        return jsonify(r)
    return "<h1>some text</h1>"


if __name__ == "__main__":
    app.run(debug=True)
