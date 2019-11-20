"""
Funkcje anonimowe
"""

# x = lambda a,b : a*b
# print(x(10, 6))
#
# lista = [('winogrona',7.99), ('jabłko',2.99), ('banan', 4.99)]
# print(sorted(lista, key=lambda x:x[1]))

# Napisz funkcje ktora z zadanej listy liczb
# wybierze elementy określone przez funkcje klucza
# lista = [1, 2, 3, 4, 5, 6]
# wybierz (lista, lambda x: x%2 == 0)
# wybierz [2, 4, 6]
#wybierz (lista, key=lambda x: x >5)
#[6]

# x = [1, 2, 3, 4, 5, 6]
#
# def wybierz(lista, funkcja):
#     wynik = []
#     for i in lista:
#         if funkcja(el) is True:
#             wynik.append(el)
#     return wynik
# print(wybierz(lista, lambda x: x%3 == 0))

# def wieksze_niz_4(x):
#     return x > 4
# print(wybierz(lista, wieksze_niz_4()))

lista = [1, 2, 3, 4, 5, 6, 7]

def przytnij(lista, start, stop):
    wynik = []
    czy_dodawac = True
    for el in lista:
        if czy_dodawac or start(el):
            wynik.append(el)
            if stop(el):
                break
    return wynik

def test_przytnij():
    rezult = przytnij(
        [1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x == 2,
        stop=lambda x: x + 1 > 6
    )
    assert rezult == [2, 3, 4, 1, 6]

    rezult = przytnij(
        (8, 9, 3, 1, 5, 12, 19, 21, 0),
        start=lambda x: x % 3 == 0,
        stop=lambda x: x % 4 == 0
    )
    assert rezult == [9, 3, 1, 5, 12]
