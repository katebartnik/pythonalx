"""
Obliczanie silni
"""

# Na podstawie rekurencji
# n! = n*(n-1)!

import time

def silnia_rek(n):
    if n <= 1:
        return 1
    else:
        return n*silnia_rek(n-1)

def silnia_iter(n):
    wynik = 1
    for i in range(1, n+1):
        wynik*=i
    return wynik

licznik = 1000

time_stan1 = time.time()
for _ in range(0, licznik):
    silnia_rek(800)
time_stan2 = time.time()

print("Czas dla rekurencji: ", time_stan2-time_stan1)

time_stan1 = time.time()
for _ in range(0, licznik):
    silnia_iter(800)
time_stan2 = time.time()

print("Czas dla uteracji: ", time_stan2-time_stan1)
