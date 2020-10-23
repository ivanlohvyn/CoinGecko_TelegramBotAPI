from flask import Flask
from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app)


@app.route("/")
def index():
    return "<h3>some text</h5>"


URL = "https://api.telegram.org/bot{}/".format(TOKEN)

if __name__ == "__main__":
    app.run(debug=True)