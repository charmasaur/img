from flask import Flask, request, render_template, url_for, make_response
import base64

import storage

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return render_template("welcome.html")

@app.route('/img/<path:path>', methods=['GET'])
def img(path):
    # TODO: Get and display the image
    return "Hello"

@app.route('/upload', methods=['POST'])
def upload():
    # TODO: Store the data and return a link
    return url_for("img", path="foo")
