import json
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import requests
from flask import Flask, redirect, request, jsonify, url_for

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def post_from_frontend(file, return_options, token):
    # Assuming `file` is a file-like object opened in binary mode
    files = {
        "file": file,
    }
    data = {
        "api_token": token,
        "return": return_options,
    }
    result = requests.post("https://api.audd.io/", files=files, data=data)
    
    return result.json()

@app.route("/", methods=["GET"])
def index():
    return "Hello, World!"


@app.route("/api", methods=["POST"])
def api():
    file = request.files.get('file')
    token = request.form.get('token')
    return_options = request.form.get('search')
    
    if file:
        filename = secure_filename(file.filename) # type: ignore
        file.save(filename)
        with open(filename, "rb") as f:
            result = post_from_frontend(f, return_options, token)
        os.remove(filename)
    else:
        result = "No file found"
        
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)
