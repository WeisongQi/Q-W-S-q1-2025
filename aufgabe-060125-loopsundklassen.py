# Aufgabe 1
txt = input("Bitte geben Sie einen Text ein: ")
x = input("Welches Zeichen soll gesucht werden? ")
count = 0
for char in txt:
    if char == x:
        count += 1
print(f"Das Zeichen {x} kommt {count} mal vor.")

# Aufgabe 2
liste = []
for i in range(5):
    zahl = int(input("Bitte geben Sie eine Zahl ein: "))
    liste.append(zahl)
print(f"Die Summe der Zahlen beträgt: {sum(liste)}")
print(f"Der Durchschnitt der Zahlen beträgt: {sum(liste)/len(liste)}")

# Aufgabe 3
hoch = int(input("Wie hoch soll der Turm sein: "))
for i in range(1, hoch + 1):
    print("*" * i)
