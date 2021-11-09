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
    return 'ok'

@app.route("/to_csv", methods=['POST'])
def to_csv():
    csv_path = request.json["csv_path"]
    seen_strings.to_csv(csv_path)
    return 'ok'

@app.route("/from_csv", methods=['POST'])
def from_csv():
    csv_path = request.json["csv_path"]
    seen_strings.from_csv(csv_path)
    return 'ok'