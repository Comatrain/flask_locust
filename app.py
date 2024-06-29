import random

from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.get("/index")
def index():
    return "Hello"


@app.get("/moreload")
def moreload():
    return str(sum([random.randint(1, 10) for _ in range(1000)]))


if __name__ == "__main__":
    serve(
        app,
        host="0.0.0.0",
        port=8000,
        threads=300,
        connection_limit=600,
    )
