class Elev:
    def __init__(self, namn, ålder, godkänd) -> None:
        self.name = str(namn)
        self.age = int(ålder)
        self.happy = godkänd

    def __str__(self):
        if self.happy:
            return f"Jag heter {self.name}. Jag är {self.age} år och just nu är jag glad!"
        else:
            return f"Jag heter {self.name}. Jag är {self.age} år och just nu är jag INTE glad!"
    def birthday(self):
        self.age += 1
        print(f"Wohoooo! Jag fyllde nyss {self.age} år!")
        self.happy = True

    def nameChange(self, newName):
        self.name = str(newName)
        self.happy = False
        print(f"Åh nej... jag behövde precis byta mitt namn till {self.name}!")

oskar = Elev("Oskar", 17, False)
print(oskar)
oskar.birthday()
print(oskar)
oskar.nameChange("Boskar")
print(oskar)