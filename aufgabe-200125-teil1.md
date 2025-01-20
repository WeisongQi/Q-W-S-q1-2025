# Aufgabe Teil1

Dieses Programm ist eine einfache Webanwendung, die mit dem Flask-Framework geschrieben wurde. Es definiert mehrere Routen, von denen jede eine einfache Zeichenkette zurückgibt.

    ````Python
        from flask import Flask


        app = Flask(__name__)
    ````
> Dieser Code importiert das Flask-Modul und erstellt eine Flask-Anwendungsinstanz.

# Begrüßungsroute
    ````Python
        @app.route("/")
        def home():
           return "Willkommen bei meiner Flask-App!"
    ````
> Diese Route definiert den Root-Pfad `/`. Wenn ein Benutzer diesen Pfad aufruft, wird "Willkommen bei meiner Flask-App!" zurückgegeben.

# Info-Route
    ````Python
        @app.route("/info")
        def info():
            return "Dies ist eine einfache API mit Flask."
    ````
> Diese Route definiert den Pfad `/info`. Wenn ein Benutzer diesen Pfad aufruft, wird "Dies ist eine einfache API mit Flask." zurückgegeben.

# Team-Route
    ````Python
        @app.route("/team")
        def team():
            return "Unser Team besteht aus IT-Experten und Entwicklern."
    ````
> Diese Route definiert den Pfad `/team`. Wenn ein Benutzer diesen Pfad aufruft, wird "Unser Team besteht aus IT-Experten und Entwicklern." zurückgegeben.

# Hilfe-Route
    ````Python
        @app.route("/hilfe")
        def hilfe():
            return "Hier finden Sie Hilfe zu unserer API."
    ````
> Diese Route definiert den Pfad `/hilfe`. Wenn ein Benutzer diesen Pfad aufruft, wird "Hier finden Sie Hilfe zu unserer API." zurückgegeben.

# Kontakt-Route
    ````Python
        @app.route("/kontakt")
        def kontakt():
            return "Schreibe uns eine E-Mail an kontakt@example.com."
    ````
> Diese Route definiert den Pfad `/kontakt`. Wenn ein Benutzer diesen Pfad aufruft, wird "Schreibe uns eine E-Mail an kontakt@example.com." zurückgegeben.

    ````Python
        if __name__ == "__main__":
            app.run(port=5000)
    ````
> Diese beiden Zeilen Code dienen dazu, die Flask-Anwendung zu starten und sie auf einem bestimmten Port auszuführen. und Der **port** 5000 kann geändert werden, aber verschiedene Firewalls haben unterschiedliche Regeln für das Öffnen von Ports.