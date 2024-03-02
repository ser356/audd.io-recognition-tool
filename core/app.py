import json
from flask_cors import CORS, cross_origin
import requests
from flask import Flask, redirect, request, jsonify, url_for

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def post_from_frontend(url, return_options, token):
    data = {
        "url": url,
        "return": return_options,
        "api_token": token,
    }
    result = requests.post("https://api.audd.io/", data=data)
    
    
    return result.json()


@app.route("/", methods=["GET"])
def index():
    return "Hello, World!"

@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()

    url = data.get("url")
    return_options = data.get("return")
    token = data.get("api_token")

    if not url or not return_options or not token:
        return jsonify({"error": "Invalid request"}), 400

    response = post_from_frontend(url, return_options, token)

    return jsonify(response)
if __name__ == "__main__":
    app.run(debug=True)
