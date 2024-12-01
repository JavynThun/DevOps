from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/version")
def get_version():
    print("v0.0.1")

@app.route("/temperature")
def hello_world():
    return "<p>Hello, World!</p>"
