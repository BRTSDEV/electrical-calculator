print("===================================")
print(" ELEKTRISCHE CALCULATOR")
print("===================================")
print("1 = Wet van Ohm")
print("2 = Elektrisch vermogen")
print("3 = Weerstanden in serie")
print("4 = Weerstanden parallel")
print("5 = Spanningsdeler")
print("6 = Wisselstroom vermogen")
print("7 = Energie van een condensator")
print("8 = Stoppen")
print("===================================")

while True:
    keuze = input("\nWat wil je berekenen? ")

    # WET VAN OHM
    if keuze == "1":
        print("\n--- WET VAN OHM ---")
        print("U = I * R")
        print("I = U / R")
        print("R = U / I")

        wat = input("Wat wil je berekenen? (U/I/R): ").upper()

        if wat == "U":
            I = float(input("Stroom I in ampere: "))
            R = float(input("Weerstand R in ohm: "))
            U = I * R
            print("Spanning =", U, "V")

        elif wat == "I":
            U = float(input("Spanning U in volt: "))
            R = float(input("Weerstand R in ohm: "))
            I = U / R
            print("Stroom =", I, "A")

        elif wat == "R":
            U = float(input("Spanning U in volt: "))
            I = float(input("Stroom I in ampere: "))
            R = U / I
            print("Weerstand =", R, "ohm")

        else:
            print("Dat klopt niet, kies U, I of R")

    # VERMOGEN
    elif keuze == "2":
        print("\n--- ELEKTRISCH VERMOGEN ---")
        print("P = U * I")

        U = float(input("Spanning in volt: "))
        I = float(input("Stroom in ampere: "))
        P = U * I
        print("Vermogen =", P, "Watt")

    # SERIE
    elif keuze == "3":
        print("\n--- WEERSTANDEN IN SERIE ---")
        print("Rtot = R1 + R2 + R3")

        R1 = float(input("R1 = "))
        R2 = float(input("R2 = "))
        R3 = float(input("R3 = "))
        Rtot = R1 + R2 + R3
        print("Totale weerstand =", Rtot, "ohm")

    # PARALLEL
    elif keuze == "4":
        print("\n--- WEERSTANDEN PARALLEL ---")
        print("1/Rtot = 1/R1 + 1/R2 + 1/R3")

        R1 = float(input("R1 = "))
        R2 = float(input("R2 = "))
        R3 = float(input("R3 = "))
        Rtot = 1 / ((1/R1) + (1/R2) + (1/R3))
        print("Totale weerstand =", Rtot, "ohm")

    # SPANNINGSDELER
    elif keuze == "5":
        print("\n--- SPANNINGSDELER ---")
        print("Uuit = Uin * R2 / (R1 + R2)")

        Uin = float(input("Ingangsspanning Uin = "))
        R1 = float(input("R1 = "))
        R2 = float(input("R2 = "))
        Uuit = Uin * R2 / (R1 + R2)
        print("Uitgangsspanning =", Uuit, "V")

    # WISSELSTROOM
    elif keuze == "6":
        print("\n--- WISSELSTROOM VERMOGEN ---")
        print("P = U * I * cos(phi)")

        U = float(input("RMS spanning = "))
        I = float(input("RMS stroom = "))
        cosphi = float(input("Vermogensfactor (0 tot 1) = "))
        P = U * I * cosphi
        print("Werkelijk vermogen =", P, "W")

    # CONDENSATOR
    elif keuze == "7":
        print("\n--- ENERGIE IN EEN CONDENSATOR ---")
        print("E = 1/2 * C * U^2")

        C = float(input("Capaciteit in Farad = "))
        U = float(input("Spanning in Volt = "))
        E = 0.5 * C * U**2
        print("Opgeslagen energie =", E, "Joule")

    # STOPPEN
    elif keuze == "8":
        print("\nProgramma wordt afgesloten...")
        print("Tot de volgende keer :)")
        break

    else:
        print("Dat is geen geldige keuze :/")

    print("-----------------------------------")
