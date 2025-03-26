import numpy as np
import datetime as dt

versuchsleiter : str = "Sophia Gwiggner"
erstellungsdatum : str = "13.03.2025"

leistungstest_exp : dict = {}

for i in range(10):
    try:
        first_experiment_id = int(i)  # Sicherstellen, dass es kein float und kein String ist
        leistungstest_exp[first_experiment_id] = { #Einfügen von den Dictionaries in das leistungstest_exp Dictionary
            "Versuchsleiter": versuchsleiter, # Versuchsleiter als Variable oben definiert, um mehr Übersicht zu schaffen
            "Erstellungsdatum": erstellungsdatum # Das Gleiche hier, ich war beim überlegen, ob ich das mit datetime machen soll, aber schaut mit String schöner aus
        }
    except (ValueError, TypeError) as j: # Sollte ein ValueError oder ein TypeError vorfallen, wird eine Fehlermeldung gebracht
        print("Folgender Fehler bei der first_experiment_id {}: {}".format(i, j))

print(leistungstest_exp)

for firstfive in range(5):
  print(firstfive, leistungstest_exp[firstfive])

# Alternativ kann man die ersten fünf auch in einem neuen dictionary ausgeben

leistungstest_exp_firstfive = {}

for firstfive in range(5):
    leistungstest_exp_firstfive[firstfive] = leistungstest_exp[firstfive]

print(leistungstest_exp_firstfive)

# Einträge mit geraden IDs

leistungstest_exp_even = {}

for firstfive in range(10):
    if firstfive % 2 == 0:
        leistungstest_exp_even[firstfive] = leistungstest_exp[firstfive]

print(leistungstest_exp_even)
