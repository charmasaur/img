from flask import abort, request, render_template, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
import base64
import imghdr

from app.storage import get, put
from app.app import app

@app.route('/', methods=['GET'])
def welcome():
    return render_template("welcome.html")

@app.route('/img/<path:path>', methods=['GET'])
def img(path):
    components = path.split(".")
    key = components[0]
    ext = ""
    if len(components) >= 2:
        ext = components[-1]

    data = get(key)
    if not data:
        return "not found", 404

    response = make_response(data)
    response.headers['Content-Type'] = 'image/' + ext
    return response

@app.route('/upload', methods=['POST'])
def upload():
    data = get_data(request)
    if not data:
        return "missing data", 400
    ext = get_ext(data)
    if not ext:
        return "could not determine type", 400
    key = put(data)
    return url_for("img", path=key + "." + ext, _external=True)

def get_data(request):
    data = None
    if 'image' in request.files:
        file = request.files['image']
        data = file.read();
    return data

def get_ext(data):
    return imghdr.what(None, h=data)
