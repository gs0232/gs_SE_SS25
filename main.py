from my_functions import build_person, build_experiment, estimate_max_hr
import numpy as np

if __name__ == "__main__":
    first_name = "Sophia"
    last_name = "Gwiggner"
    sex = "female"
    age_years = 20
    age = age_years
    experiment_name = "sakai_3_max_hr"
    date = "23.03.2025"
    supervisor = "Julian Huber"

    first_person = build_person(first_name, last_name, sex, age)
    print("Die Testperson:", first_person)

    subject = first_person

    first_experiment = build_experiment(experiment_name, date, supervisor, subject)
    print("Das Experiment:", first_experiment)

    estimated_hr = estimate_max_hr(age_years, sex)
    print("Die Herzfrequenz:", estimated_hr)

# Klasse Sensor

class Sensor():
    """
    A Sensor calss taht represents a sensor!
    """
    def __init__(self, id):
        self.id = id
        self.messwert = None
        self.messwerte = []
        self.__password = "123456" # zwei Unterstriche zum Schützen

    def measure(self, messwert):
        self.messwert = messwert
        self.messwerte.append(messwert)

    def calc_mean(self):
        self.mittelwert = sum(self.messwerte)/len(self.messwerte)
        return self.mittelwert
    
    def reset(self, eingabe_password):
        # eingabe_password = input("Eingabe Passwort:") --> schöne Abfrage des Passworts
        if eingabe_password == self.__password:
            print("Instanz wurde zurückgesetzt")
        else:
            print("Wrong password")

if __name__ == "__main__":
    s1 = Sensor(123) # Sensor Instanz ertstellt mit ID: 123
    print(s1.id)
    s1.measure(1) # Messwert
    s1.measure(3) # Messwert
    s1.measure(7) # Messwert --> werden in Liste (messwerte) hinzugefügt, weil in Funktion measure ... append steht
    print(s1.messwerte)
    print(s1.calc_mean())
    print(s1.__dict__) # Sensor 1 (ID: 123) wird als Dicitonary ausgegeben
    print(s1.reset("123456"))
    print(s1.reset("654321"))
    # das_passwort = s1.__password --> wäre oben kein doppeleter Unterstrich, könnte man hier einfach das Passwort klauen
    # print(s1.reset(das_passwort)) --> Hier wird jetzt eine Fehlermeldung gegeben, weil doppelte Unterstrich das Passwort versteckt
