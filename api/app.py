from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import random

import sqlite3

app = Flask(__name__, template_folder="templates", static_url_path="")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///joke.db"

db = SQLAlchemy(app)

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.String(150), nullable=False)

    def __init__(self, joke):
        self.joke = joke


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get/")
def get_page():
    return render_template("get.html")


@app.route("/get/random")
def return_random_joke():

    random_id = random.randrange(1, 4650)
    with app.app_context():
        joke = Joke.query.filter_by(id=random_id).first()

        return str(joke.joke)


@app.route("/get/id/<int:id>")
def id_joke(id):
    
    with app.app_context():
        joke = Joke.query.filter_by(id=id).first()

        return str(joke.joke)


if __name__ == "__main__":

    app.run()
