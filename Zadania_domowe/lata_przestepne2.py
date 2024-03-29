# Pierwszy prtzykład rozwiązania zadania

def czy_przestepny(rok):
    return rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0)

# Drugi przykład rozwiązania zadania
def lata_przestepne(rok_od, rok_do):
    if rok_od>rok_do:
        return None

    lata = list()
    for rok in range(rok_od, rok_do + 1):
        if czy_przestepny(rok):
            lata.append(rok)
    return lata
print(lata_przestepne(2000, 2030))

def test_lata_przestepne():
    assert lata_przestepne(2020, 2030) == [2020, 2024, 2028]
