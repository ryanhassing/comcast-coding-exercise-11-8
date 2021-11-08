from flask import Flask

app = Flask(__name__)

seen_strings = {}
# TODO load to/from database?

@app.route("/stats")
def hello():
    print("stats here")

@app.route("/add")
def add_string(s: str):
    print("add string here")