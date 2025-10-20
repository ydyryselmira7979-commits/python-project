# third.py

def je_prvocislo(cislo):
    """Vrátí True, pokud je číslo prvočíslem, jinak False."""
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False
    for i in range(3, int(cislo ** 0.5) + 1, 2):
        if cislo % i == 0:
            return False
    return True


def vrat_prvocisla(maximum):
    """Vrátí seznam všech prvočísel od 1 do maximum (včetně)."""
    prvocisla = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            prvocisla.append(i)
    return prvocisla


# Testy podle zadání
if __name__ == "__main__":
    print(je_prvocislo(1))    # False
    print(je_prvocislo(2))    # True
    print(je_prvocislo(3))    # True
    print(je_prvocislo(100))  # False
    print(je_prvocislo(101))  # True

    print(vrat_prvocisla(1))   # []
    print(vrat_prvocisla(2))   # [2]
    print(vrat_prvocisla(3))   # [2, 3]
    print(vrat_prvocisla(10))  # [2, 3, 5, 7]
