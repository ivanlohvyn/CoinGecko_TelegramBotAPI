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


def main():
    r = requests.get(URL + "getMe")
    write_json(r.json())


if __name__ == "__main__":
    app.run(debug=True)