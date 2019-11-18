"""
Funkcje anonimowe
"""

x = lambda a,b : a*b
print(x(10, 6))

lista = [('winogrona',7.99), ('jabłko',2.99), ('banan', 4.99)]
print(sorted(lista, key=lambda x:x[1]))
