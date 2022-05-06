from distutils.log import debug
from socket import herror
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"