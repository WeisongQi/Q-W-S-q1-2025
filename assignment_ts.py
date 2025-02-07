def begruessung(name):  # syntax error
    print("Hallo, " + name)  # syntax error und Name ist nicht definiert


def addiere_zahlen(a, b):  # syntax error
    ergebnis = a + b  # syntax error
    return ergebnis  # NameError


def subtrahiere_zahlen(a, b):  # b ist nicht genutzt
    return a - b  # c ist nicht definiert


def main():  # syntax error
    zahl1 = int(input("Gib eine Zahl ein: "))
    zahl2 = int(input("Gib eine weitere Zahl ein: "))

    summe = addiere_zahlen(zahl1, zahl2)  # TypeError
    print(f"Die Summe ist:   {summe}")  # TypeError

    differenz = subtrahiere_zahlen(zahl1, zahl2)  # TypeError
    print(f"Die Differenz ist:   {differenz}")  # TypeError

    begruessung("Max")  # TypeError


if __name__ == "__main__":  # syntax error
    main()
