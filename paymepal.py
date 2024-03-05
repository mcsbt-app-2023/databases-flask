import hashlib
from flask import Flask, render_template, request, session, redirect
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["SECRET_KEY"] = "very secret stuff"
engine = create_engine("sqlite:///paymepal.db")


def hash_value(string):
    hash = hashlib.sha1()
    hash.update(string.encode())
    return hash.hexdigest()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    pass


@app.route("/admin")
def admin():
    pass


app.run(debug=True, port=8080)
