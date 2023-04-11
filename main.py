from flask import Flask

import config as conf

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run(host=conf.FLASK_HOST, port=int(conf.FLASK_PORT))
