# Wörterbuch erstellen und Abfragen

eng_de = {}


def add_word(eng, de):
    eng_de[eng] = de
    eng_de[de] = eng


add_word("apple", "Apfel")
add_word("banana", "Banane")
add_word("cherry", "Kirsche")
add_word("car", "Auto")
add_word("bus", "Bus")
add_word("train", "Zug")
add_word("plane", "Flugzeug")
add_word("ship", "Schiff")
add_word("bike", "Fahrrad")
add_word("motorcycle", "Motorrad")
add_word("truck", "Lastwagen")
add_word("lorry", "LKW")

# print(eng_de.keys())
while True:
    input_word = input("Bitte geben Sie ein Wort ein: ")
    if input_word == "exit":
        break
    elif input_word == "list":
        print(eng_de.keys())
    # print(eng_de.get(input_word, "Das Wort ist nicht im Wörterbuch"))
    print(f"{input_word}: {eng_de.get(input_word, 'Das Wort ist nicht im Wörterbuch')}")


my_dict = {"apfel": "Apple", "wörterbuch": "dictionary"}
my_userinput = input("Gib ein deutsches Wort ein: ")
if my_userinput in my_dict:
    print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")
else:
    actual_translation = input(
        "Das Wort gibt es noch nicht, gib die engl. Übersetzung ein: "
    )
    my_dict[my_userinput] = actual_translation
    print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")

git_commands = {
    "pull": 'Der "pull"-Befehl wird verwendet, um Änderungen von einem entfernten Repository in das lokale Repository zu holen und zu integrieren.',
    "push": 'Der "push"-Befehl wird verwendet, um Änderungen vom lokalen Repository in das entfernte Repository hochzuladen.',
    "commit": 'Der "commit"-Befehl speichert Momentaufnahmen der Dateien im lokalen Repository.',
    "clone": 'Der "clone"-Befehl erstellt eine Kopie eines bestehenden Repositories in ein neues Verzeichnis.',
    "branch": 'Der "branch"-Befehl listet, erstellt oder löscht Zweige im Repository.',
}


def git_command_description(command):
    return git_commands.get(command, "Unbekannter Git-Befehl.")


# Beispielverwendung
command = "pull"
print(git_command_description(command))
