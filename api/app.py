from flask import Flask, request, jsonify, render_template
import dbmanager as db
import threading

app = Flask(__name__, template_folder="templates", static_url_path="")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_page():
    return render_template("get.html")


@app.route("/get/random")
def random_joke():
    joke = db.random_joke()

    req = {}
    req["id"] = joke[0][0]
    req["question"] = joke[0][1]
    req["answer"] = joke[0][2]

    return jsonify(req)


@app.route("/get/id/<int:id>")
def id_joke(id):
    joke = db.with_id(id)

    req = {}
    req["id"] = joke[0][0]
    req["question"] = joke[0][1]
    req["answer"] = joke[0][2]

    return jsonify(req)


if __name__ == "__main__":
    app.run(debug=True)
