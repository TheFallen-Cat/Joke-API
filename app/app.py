from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import random
import os


app = Flask(__name__, template_folder="templates", static_url_path="", static_folder="static")

base_directory = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_directory, 'database/jokes.db')


db = SQLAlchemy(app)

cors = CORS(app=app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Joke(db.Model):
    __tablename__ = 'joke'
    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.String(150), nullable=False)

    def __init__(self, joke):
        self.joke = joke


# Return 404 Error if page not found
@app.errorhandler(404)
@cross_origin()
def not_found_error(error):
    return render_template("page404.html")


# Home Page
@app.route("/")
@cross_origin()
def home():
    return render_template("api.html")

# Get Random jokes
@app.route("/random")
@cross_origin()
def return_random_joke():

    no_of_rows = Joke.query.count()

    random_id = random.randrange(1, no_of_rows)

    joke = Joke.query.filter_by(id=random_id).first()

    json_joke = {'id':joke.id, 'main_joke':joke.joke}

    return json_joke

# Get Jokes with their ID
@app.route("/id/<int:id>")
@cross_origin()
def id_joke(id):
    
    joke = Joke.query.filter_by(id=id).first()

    json_joke = {'id':joke.id, 'main_joke':joke.joke}

    return json_joke



if __name__ == "__main__":

    app.run()




        
