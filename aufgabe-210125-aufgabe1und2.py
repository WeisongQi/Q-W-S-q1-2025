from flask import Flask, request, jsonify
from users import users

app_1 = Flask(__name__)

app_2 = Flask(__name__)


@app_1.route("/", methods=["GET"])
def home():
    return "Welcome Mamazon"


@app_1.route("/brand/<id>", methods=["GET"])
def get_brand_by_id(id):
    type = request.args.get("type")
    condition = request.args.get("condition")
    # Brand-ID: 10, Type: clothes, Condition: new
    return f"Brand-ID: {id}, Type: {type}, Condition: {condition}"


@app_1.route("/product/<product_id>", methods=["GET"])
def get_item(product_id):
    # Product-ID: 123
    return f"Product-ID: {product_id}"


@app_1.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    # Searching for: shoes
    return f"Searching for: {query}"


@app_2.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome Anmeldung"}), 200


@app_2.route("/user/<id>", methods=["GET"])
def user(id):
    try:
        user_id = int(id)
        if user_id == users[user_id - 1]["id"]:
            return (
                jsonify(
                    {
                        "message": f"User {users[user_id -1]['name']} is Nr.{id} , Email: {users[user_id-1]['email']} "
                    }
                ),
                200,
            )
        else:
            return jsonify({"error": "Fehler, falls id nicht existiert."}), 400
    except (IndexError, ValueError):
        return jsonify({"error": "Fehler, falls id nicht existiert."}), 400


@app_2.route("/login/<id>", methods=["GET"])
def login(id):
    try:
        user_id = int(id)
        if user_id == users[user_id - 1]["id"]:
            return (
                jsonify(
                    {
                        "message": f"User {users[user_id -1]['name']} successfully logged in"
                    }
                ),
                200,
            )
        else:
            return jsonify({"error": "Fehler, falls id nicht existiert."}), 400
    except (IndexError, ValueError):
        return jsonify({"error": "Fehler, falls id nicht existiert."}), 400


@app_2.route("/search", methods=["GET"])
def search():
    u_name = request.args.get("name")
    for user in users:
        if user["name"] == u_name:
            return jsonify({"message": f" Found user: {user['name']}"}), 200
    return jsonify({"error": f"No user found with name {u_name}."}), 404


if __name__ == "__main__":
    while True:
        up = input("Which app do you want to run? (1/2): ")
        if up == "1":
            app_1.run(debug=True, port=6060)
            break
        elif up == "2":
            app_2.run(debug=True, port=6060)
            break
        else:
            print("Invalid input. Please enter 1 or 2.")
