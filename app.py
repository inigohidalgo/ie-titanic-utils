
from flask import Flask, request
from ie_utils import tokenize

app = Flask(__name__)

@app.route("/")
def home():
    print(request.args)
    return "AdVaNcEd🐍PyThOn"

@app.route("/tokenize")
def do_tokenize():
    sentence=request.args["sentence"]
    return str(tokenize(sentence))
