# Aufgabe eine Klasse für Haustier


class Haustier:
    def __init__(self, name, species, age, favorite_food, food, energy_level):
        self.nameDesHaustier = name
        self.tierart = species
        self.alterInJahren = age
        self.lieblingsessen = favorite_food
        self.food = food
        self.energy_level = energy_level

    def get_description(self):
        print(
            f"{self.nameDesHaustier} ist ein {self.alterInJahren} alter {self.tierart}, hat {self.energy_level} %."
        )

    def feed(self):
        f = input(
            f"Bitte wählen Sie das Futter ({self.lieblingsessen} oder {self.food}) für {self.tierart} - {self.nameDesHaustier} : "
        )
        if f == self.lieblingsessen:
            self.energy_level += 30
            print(
                f"{self.tierart} - {self.nameDesHaustier} liebt {self.lieblingsessen} ! Die Energy ist jetzt {self.energy_level} % ."
            )
        elif f == self.food:
            self.energy_level += 10
            print(
                f"{self.tierart} - {self.nameDesHaustier} hat {self.food} gegessen. Die Erergie ist jetzt {self.energy_level} % ."
            )

    def play(self):
        duration = int(
            input(
                f"Wie lange (in Minuten) willst du mit {self.tierart} - {self.nameDesHaustier} spielen ? "
            )
        )
        verbrauch_energy = duration * 5
        if self.energy_level <= verbrauch_energy:
            self.energy_level = self.energy_level - verbrauch_energy
            print(
                f"{self.tierart} - {self.nameDesHaustier} ist müde, muss sich schlafen oder essen."
            )
        else:
            self.energy_level = self.energy_level - verbrauch_energy
            print(
                f"{self.tierart} - {self.nameDesHaustier} hat {duration} Minuten gespielt und hat jetzt {self.energy_level} % Energie."
            )

    def sleep(self):
        relex = int(
            input(
                f"Wie lange (in Stunden) willst du  {self.tierart} - {self.nameDesHaustier} schlafen ? "
            )
        )
        new_energy = relex * 20
        if self.energy_level + new_energy >= 100:
            self.energy_level = 100
            print(f"{self.tierart} - {self.nameDesHaustier} ist wieder Da .")
        else:
            self.energy_level = self.energy_level + new_energy
            print(
                f"{self.tierart} - {self.nameDesHaustier} muss noch {self.energy_level / 20} Stunden schlafen."
            )


# haustier = Haustier("mimi", "katze", "3 Jahre", "fisch", "cat-manu", 100)
# haustier.get_description()
# haustier.feed()
# haustier.play()
# haustier.sleep()


# Main
def main():
    haustiere = []

    while True:
        print("\nMenü:")
        print("1. Erstelle ein neues Haustier")
        print("2. Zeige alle Haustiere")
        print("3. Füttere ein Haustier")
        print("4. Spiele mit einem Haustier")
        print("5. Lass ein Haustier schlafen")
        print("6. Beende das Programm")

        wahl = input("Wähle eine Option: ")

        if wahl == "1":
            name = input("Name des Haustiers: ")
            species = input("Tierart: ")
            age = input("Alter: ")
            favorite_food = input("Lieblingsessen: ")
            food = input("Food: ")
            energy_level = int(input("Energielevel: "))
            haustier = Haustier(name, species, age, favorite_food, food, energy_level)
            haustiere.append(haustier)
            print(f"{name} wurde erstellt.")
        elif wahl == "2":
            for i, haustier in enumerate(haustiere):
                print(f"\nHaustier {i + 1}:")
                haustier.get_description()
        elif wahl == "3":
            index = (
                int(input("Welches Haustier möchtest du füttern (Nummer eingeben): "))
                - 1
            )
            if 0 <= index < len(haustiere):
                haustiere[index].feed()
            else:
                print("Ungültige Nummer.")
        elif wahl == "4":
            index = (
                int(
                    input(
                        "Mit welchem Haustier möchtest du spielen (Nummer eingeben): "
                    )
                )
                - 1
            )
            if 0 <= index < len(haustiere):
                haustiere[index].play()
            else:
                print("Ungültige Nummer.")
        elif wahl == "5":
            index = int(input("Welches Haustier soll schlafen (Nummer eingeben): ")) - 1
            if 0 <= index < len(haustiere):
                haustiere[index].sleep()
            else:
                print("Ungültige Nummer.")
        elif wahl == "6":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Wahl. Bitte versuche es erneut.")


if __name__ == "__main__":
    main()
