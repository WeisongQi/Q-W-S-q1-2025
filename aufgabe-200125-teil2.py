from flask import Flask

w_s_app = Flask(__name__)


# Begrüßungsroute
@w_s_app.route("/")
def home():
    return "Willkommen bei meiner Flask-App!"


# Begrüßungsroute Zusatz
@w_s_app.route("/greet/<name>")
def greet(name):
    return f"Hallo {name}, Willkommen auf meiner Flask-API!"


# About-Route
@w_s_app.route("/about")
def about():
    return "Mein Name ist Qi, Vorname ist Weisong. und Ich hoffe, ich kann die Fähigkeiten, die ich gelernt habe, nutzen, um eine bessere Welt zu bauen."


# Projekt-Route
@w_s_app.route("/projekt")
def projekt():
    return "Mein aktuelles Projekt ist eine Flask-API für Anfänger."


# News-Route
@w_s_app.route("/news")
def news():
    return "Heute lernen wir, wie man APIs mit Flask erstellt! und Ports erstellen"


# Feedback-Route
@w_s_app.route("/feedback")
def feedback():
    return "Wir freuen uns über dein Feedback unter feedback@example.com."


# Support-Route
@w_s_app.route("/support")
def support():
    return "Besuche unsere Support-Seite unter support.example.com."


# S-Route
@w_s_app.route("/item/<product_id>")
def get_item(product_id):
    return f"Besuche unsere Support-Seite unter {product_id}."


if __name__ == "__main__":
    w_s_app.run(debug=True, port=7000)
