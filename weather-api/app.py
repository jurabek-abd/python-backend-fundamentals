from flask import Flask
from utils.error_handler import register_error_handlers

app = Flask(__name__)
register_error_handlers(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
