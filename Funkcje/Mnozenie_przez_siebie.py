# Napisz funkcje która wymnoży przez siebie elementy podane w liscie wejsciowej (lista)

n = [1, 2, 3]

def silnia_iter(n):
    wynik = 1
    for i in n:
        wynik*=i
    return wynik
print(silnia_iter(n))

x = [1, 2]

def silnia_iter(x):
    wynik = 1
    for i in x:
        wynik*=i
    return wynik
print(silnia_iter(x))

# Napisz funkcje która wybierze i zwróci z podanego napisu liste liczb
# x = "a1b2c1d2"
# [1, 2, 1, 2]
# x = "a100v300"
# [1,0,0, 2, 0, 0]

def wybierz_cyfry(napis):
    wynik = []
    for litera in napis:
        if litera.isdigit():
            wynik.append(litera)
    return wynik

x = "a1b2c1d2"
print(wybierz_cyfry(x))