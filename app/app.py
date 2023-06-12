from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import random

import os

app = Flask(__name__, template_folder="templates", static_url_path="", static_folder="static")

base_directory = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_directory, 'database/jokes.db')


db = SQLAlchemy(app)

class Joke(db.Model):
    __tablename__ = 'joke'
    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.String(150), nullable=False)

    def __init__(self, joke):
        self.joke = joke
    

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/")
def get_page():
    return render_template("api.html")


@app.route("/api/random")
def return_random_joke():

    no_of_rows = Joke.query.count()

    random_id = random.randrange(1, no_of_rows)

    joke = Joke.query.filter_by(id=random_id).first()

    json_joke = {'id':joke.id, 'main_joke':joke.joke}

    return json_joke

@app.route("/api/id/<int:id>")
def id_joke(id):
    
    joke = Joke.query.filter_by(id=id).first()

    json_joke = {'id':joke.id, 'main_joke':joke.joke}

    return json_joke


@app.route("/about/")
def about_page():

    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

