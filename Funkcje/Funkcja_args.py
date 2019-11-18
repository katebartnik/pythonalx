"""
Funkcja z dowolna iloscia parametrów
"""
#Funkcja mnoży wartości podane do jej środka
#Możliwe podanie nieznanej liczby parametrów

def iloczn(start, *args):
    wynik = start
    for _, arg in enumerate(args,100):
        #print(f"Pozycja {nr} = {arg}")
        wynik *= arg
    return wynik

print(iloczn(2,1, 2, 3, 4, 5))