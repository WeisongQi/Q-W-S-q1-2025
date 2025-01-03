# Git-Befehl Wörterbuch erstellen und Abfragen

# Git-Befehlswörterbuch erstellen
git_commands = {
    "init": "Ein neues Git-Repository erstellen",
    "clone": "Ein bestehendes Repository klonen",
    "status": "Den Status des Arbeitsverzeichnisses anzeigen",
    "add": "Dateien zum Staging-Bereich hinzufügen",
    "commit": "Dateien aus dem Staging-Bereich committen",
    "push": "Commits zum Remote-Repository hochladen",
    "pull": "Änderungen vom Remote-Repository abrufen und zusammenführen",
    "branch": "Zweige auflisten, erstellen oder löschen",
    "checkout": "Zu einem bestimmten Zweig oder Commit wechseln",
    "merge": "Einen bestimmten Zweig in den aktuellen Zweig zusammenführen",
    "log": "Commit-Log anzeigen",
    "diff": "Unterschiede zwischen Commits anzeigen",
    "reset": "Den aktuellen Zweig auf einen bestimmten Zustand zurücksetzen",
    "rm": "Dateien aus dem Arbeitsverzeichnis und dem Staging-Bereich entfernen",
    "stash": "Aktuelle Änderungen im Arbeitsverzeichnis zwischenspeichern",
    "rebase": "Änderungen des aktuellen Zweigs auf einen anderen Zweig anwenden",
}


# Funktion zur Abfrage der Git-Befehlsbeschreibung
def query_git_command(command):
    return git_commands.get(command, "Unbekannter Git-Befehl")


# abfrage
if __name__ == "__main__":
    while True:
        command = input(
            "Bitte geben Sie den zu abfragenden Git-Befehl ein (oder 'exit' zum Beenden): "
        )
        if command.lower() == "exit":
            print("Programm beendet.")
            break
        description = query_git_command(command)
        print(f"{command}: {description}")
