"""

lista = (-2, 10, 0, 5, 1, 16, 9)

wybierz z przedziału(lista, 5, 10)
"""

lista = (-2, 10, 0, 5, 1, 16, 9)

def przedzial_wybierz(lista, a, b):
    wynik = []
    for i in lista:
        if a <= i <= b:
            wynik.append(i)
    return wynik

def test_przedzial_pusta_lista():
    assert przedzial_wybierz([], 10, 20) == []

def test_przedzial_wybierz():
    assert przedzial_wybierz([1, 10, 11, 20, 30], 10, 20) == [10, 11, 20]

