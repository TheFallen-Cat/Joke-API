from flask import Flask, request, jsonify
import dbmanager as db

app = Flask(__name__)


@app.route("/home")
def home():
    return "This is the home page."


@app.route("/random")
def return_joke():
    joke = db.random_joke()

    req = {}
    req["id"] = joke[0][0]
    req["joke"] = joke[0][1]

    return jsonify(req)


if __name__ == "__main__":
    app.run()
