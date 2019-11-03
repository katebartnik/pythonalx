# Zadanie domowe
# Postaraj się w jakiejś formie zwizualizować położenia na planszy
"""
To jest plansza bez gracza
0000
0000
0000
0000

Plansza z grczem:
0000
00G0
0000
0000

wcisam s:
0000
0000
00G0
0000

ide w lewo i trafiam na skarb
0000
0000
0S00
0000

plansza = [[0,0,0,0],[0,0,0,0],[0,S,0,0],[0,0,0,0]]

"""

playerPositionX = int(input("podaj pozucję x gracza:")) - 1 #musimy przetransformować wartość inputową na wartość indeksową
playerPositionY = int(input("podaj pozucję y gracza:")) - 1

for i in range(5):
    print('')
    for j in range(5):
        if playerPositionX == j and playerPositionY == i:
            print("G", end=" ")
        else:
            print("0", end=" ")
