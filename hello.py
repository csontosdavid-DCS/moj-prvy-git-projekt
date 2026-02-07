# Moja prvá Python aplikácia
def pozdrav(meno, jazyk="sk"):
    if jazyk == "sk":
        print(f"Ahoj {meno}!")
    elif jazyk == "en":
        print(f"Hello {meno}!")

def rozlucka(meno, jazyk="sk"):
    if jazyk == "sk":
        print(f"Dovidenia {meno}!")
    elif jazyk == "en":
        print(f"Goodbye {meno}!")

pozdrav("David", "sk")
rozlucka("David", "sk")
