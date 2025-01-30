def begruessung name:       # syntax error
print("Hallo, " + Name)     # syntax error und Name ist nicht definiert

def addiere_zahlen(a, b)    # syntax error
    ergebnis = a + b        # syntax error
    return ergebis          # NameError

def subtrahiere_zahlen(a, b): # b ist nicht genutzt
    return a - c          # c ist nicht definiert

def main()                # syntax error
    zahl1 = input("Gib eine Zahl ein: ")  
    zahl2 = input("Gib eine weitere Zahl ein: ")  

    summe = addiere_zahlen(zahl1, zahl2)        # TypeError
    print("Die Summe ist: " + summe)        # TypeError

    differenz = subtrahiere_zahlen(zahl1, zahl2)        # TypeError
    print("Die Differenz ist: " + differenz)    # TypeError

    begruessung("Max")          # TypeError

if __name__ = "__main__":       # syntax error
    main()
