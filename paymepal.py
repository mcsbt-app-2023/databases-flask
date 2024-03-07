import hashlib
from flask import Flask, render_template, request, session, redirect
from sqlalchemy import create_engine, text

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
    user = request.form["user"]
    password = hash_value(request.form["password"])

    query = text(
        f"""
        SELECT username, password
        FROM users
        WHERE username=:username AND password=:password
        """
    )
    user_found = False

    with engine.connect() as connection:
        results = connection.execute(query, username=user, password=password)

        for user in results:
            user_found = True

    if user_found:
        return "OK"
    else:
        return "user not found", 403


@app.route("/admin")
def admin():
    pass


app.run(debug=True, port=8080)
