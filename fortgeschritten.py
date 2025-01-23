from flask import Flask, request
from date.users_list import users

import json

# import os

app = Flask(__name__)
# users = {}


# def save_users(users):
#     with open("data.users.json", "w") as file:
#         json.dump(users, file, indent=4)


# def load_users():
#     if os.path.exists("date.users.json"):
#         with open("date.users.json", "r") as file:
#             return json.load(file)
#     else:
#         from date.users_list import users

#         save_users(users)
#         return users


# users = load_users()


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    final_user = None

    for u in users:
        if u["id"] == user_id:
            final_user = u

    if final_user == None:
        return "User could not be found "

    return f"The User is {final_user}"


# Route 3: /search?name=<name>
# Beispiel: http://localhost:6060/search?name=Charlie
# Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"
@app.route("/search", methods=["GET"])
def get_user_by_name():
    final_user = None
    name = request.args.get("name")
    for u in users:
        if u["firstName"] == name:
            final_user = u

    if final_user == None:
        return "User could not be found "

    return f"The User is {final_user}"


# 1. Postman installieren
# 2. url eingeben, POST Befehl aushwählen --> siehe Screenshot
# 3. Ausführen und veschiedene Parameter im  body angeben
# 4. Versuchen den richtigen Benutzer zu bekommen
# 5. Versucht eine weitere post anfrage mit signup zu erstellen,
# welche Route einen neuen Nutzer in die Liste einfügt
# 6. Zusatz: Wendet sinvolle Fälle für PUT und DELETE an (z.B udpate username, delete user)
# 7. Schwierig: Schreibt die Nutzer-liste in eine Datei, sodass die Liste aktuell bleibt, auch nach Beenden des Program
@app.route("/users/login", methods=["POST"])
def login():
    credentials = request.get_json()
    username = credentials["username"]
    password = credentials["password"]

    final_user = None
    for u in users:
        if u["username"] == username:
            final_user = u

    if final_user == None:
        return "User could not be found "
    # Now you can access the user based on email and password and return if valid credentials
    return f"Hallo {credentials} {username} {password}"


@app.route("/users/signup", methods=["POST"])
def signup():
    new_user = request.get_json()
    new_user["id"] = max([u["id"] for u in users], default=0) + 1
    users.append(new_user)
    with open("date.users.json", "w") as file:
        json.dump(users, file, indent=4)
    # save_users(users)
    return f"User {new_user} added successfully"


@app.route("/users/update/<int:id>", methods=["PUT"])
def update_user(id):
    updated_user = request.get_json()
    for u in users:
        if id == u["id"]:
            u.update(updated_user)
            # save_users(users)
            return f"User {updated_user} updated successfully"
    return "User not found"


@app.route("/users/del", methods=["DELETE"])
def delete_user():
    user_name = request.args.get("username")
    for u in users:
        if user_name == u["username"]:
            users.remove(u)
            # save_users(users)
            return f"User {user_name} deleted successfully"
    return "User not found"


if __name__ == "__main__":
    app.run(debug=True, port=6060)
