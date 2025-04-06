# Klassen Definition

class Pferd():
    def __init__(self, pferd_name, pferd_groesse):
        print("Hier wird ein Pferd geboren")
        print("Das Pferd ist", pferd_groesse, "groß")

        # Ein Attribut hinzufügen
        self.groesse = pferd_groesse
        self.name = pferd_name

    def sich_vorstellen(self):
        print("Ich bin", self.name, "und", self.groesse, "groß")

    def laufen(self, geschwindigkeit):
        self.geschwindigkeit = geschwindigkeit  # Fix: richtige Schreibweise
        print("Ich bin", self.geschwindigkeit, "schnell")

    def __str__(self):  # Optional: Bessere Darstellung
        return f"Pferd {self.name}, Größe: {self.groesse}"


# Instanzierung eines Objekts

pf1 = Pferd("Beauty", "1,70 m")  # self müssen wir nie übergeben
pf2 = Pferd("Black", "2,20 m")

print(pf2.groesse)

pf1.sich_vorstellen()
pf2.sich_vorstellen()

pf1.laufen("30 km/h")
print(pf1.geschwindigkeit)  # Fix: richtige Variable

class Sattel(Pferd):

    def sattel_farbe(self, farbe):
        self.sattelfarbe = farbe
        print("Die Farbe ist", self.sattelfarbe)


otto = Sattel("pink")
print(otto.id)