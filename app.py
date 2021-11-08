from flask import Flask, request
from Seen_Strings import Seen_Strings

app = Flask(__name__)

seen_strings: Seen_Strings = Seen_Strings()

@app.route("/stats", methods=['GET'])
def stats():
    return seen_strings.stats()

@app.route("/add", methods=['POST'])
def add_string():
    s = request.json["string"]
    seen_strings.add(s)