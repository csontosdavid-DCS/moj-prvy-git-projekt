def pozdrav(meno, jazyk="sk"):
    if jazyk == "sk":
        print(f"Ahoj {meno}!")
    elif jazyk == "en":
        print(f"Hello {meno}!")

pozdrav("David", "en")