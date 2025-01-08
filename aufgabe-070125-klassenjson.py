# Aufgabe 1.1
class Zutat:
    def __init__(self, name, kalorien, zeit):
        self.name = name
        self.kalorien_pro_100g = kalorien
        self.zubereitungszeit = zeit


# Aufgabe 1.2
class Rezept:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung
        self.zutatenliste = {}

    def zutat_hinzufügen(self, zutat, menge):
        self.zutatenliste[zutat] = menge

    def kalorien(self):
        total_kalorien = 0
        for zutat, menge in self.zutatenliste.items():
            menge_in_g = int(menge.replace("g", ""))
            total_kalorien += (zutat.kalorien_pro_100g / 100) * menge_in_g
        print(f"Gesamtkalorien: {total_kalorien}")

    def kochzeit(self):
        max_kochzeit = 0
        for zutat in self.zutatenliste.keys():
            if zutat.zubereitungszeit > max_kochzeit:
                max_kochzeit = zutat.zubereitungszeit
        print(f"Längste Kochzeit: {max_kochzeit} Minuten")

    def rezept_anzeigen(self):
        print(f"Rezept: {self.name}")
        print("Zutaten:")
        for zutat, menge in self.zutatenliste.items():
            print(f"{zutat.name}: {menge}")
        print(f"Beschreibung: {self.beschreibung}")


# Beispiel
Tomate = Zutat("Tomate", 18, 5)
Zwiebel = Zutat("Zwiebel", 40, 10)
Knoblauch = Zutat("Knoblauch", 149, 2)

rezept = Rezept("Tomatensuppe", "Eine leckere Tomatensuppe.")
rezept.zutat_hinzufügen(Tomate, "200g")
rezept.zutat_hinzufügen(Zwiebel, "100g")
rezept.zutat_hinzufügen(Knoblauch, "10g")

rezept.rezept_anzeigen()
rezept.kalorien()
rezept.kochzeit()

# print(rezept.zutatenliste.items())

# print(rezept.zutatenliste)

# Aufgabe 2

import requests

area_name = input("Welche Stadt möchtest du wissen? ")
response = requests.get(f"https://wttr.in/{area_name}?format=j1")
daten = response.json()
# jetzt sind die json daten in der variable daten gespeichert
# print(daten)
# print(daten["current_condition"][0]["temp_C"])
temperatur = daten["current_condition"][0]["temp_C"]
wetter = daten["current_condition"][0]["weatherDesc"][0]["value"]
print(wetter)
print(f"The weather in {area_name} is {wetter} with {temperatur}°C")
