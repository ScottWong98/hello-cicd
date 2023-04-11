import os

import config as conf
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"Hello World"


if __name__ == "__main__":
    app.run(host=conf.FLASK_HOST, port=int(conf.FLASK_PORT))
