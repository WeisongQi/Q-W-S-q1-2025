from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)


def w_json(menu_l):
    with open("dates.json", "w") as file:
        json.dump(menu_l, file, indent=4)


def r_json():
    if not os.path.exists("dates.json"):
        w_json([])
    with open("dates.json", "r") as file:
        return json.load(file)


# Lokale Datenbank


@app.route("/", methods=["GET"])
def home():
    return "Welcome recipes"


@app.route("/input", methods=["POST"])
def input():
    dates = r_json()
    date_new = request.get_json()
    date_new["id"] = max([m["id"] for m in dates], default=0) + 1
    dates.append(date_new)
    w_json(dates)
    return jsonify(f"menu {date_new['Name']} is inputted"), 200


@app.route("/output", methods=["GET"])
def output():
    dates = r_json()
    return jsonify(dates), 200


app.run(debug=True, port=6060)
