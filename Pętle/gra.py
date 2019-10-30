import random
DEBUG = True

#losowanie poczatkowego polozenia

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)


skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)


#Obliczam odległość po wylosowaniu

odleglosc_po_wylosowaniu = abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)
print(odleglosc_po_wylosowaniu)

#W zaleznosci od wartosci zmiennej DEGUB printuje info o polozeniu skarbu gracza

if DEBUG:
    print(f"Położenie gracza (x={gracz_x}, y = {gracz_y})")
    print(f"Położenie skarbu (x={skarb_x}, y = {skarb_y})")
    print(f"Minimalna liczba ruchów = {odleglosc_po_wylosowaniu}")

print("""""
Witaj!
Twoim zadaniem jest odnalezienie skarbu!
Twoje komendy:
W - góra
A - lewo
S - dół
D - prawo

Uważaj możesz wypaśc poza planszę!
Po każdym ruchu mozesz dostac info czy sie zblizasz czy oddalasz
""""")

while True:
 #pytamy gracza o ruch

    ruch == input("Wpisz komendę (a-lewo, d-prawo, w-góra, s-dół)")
#zmianiamy pozycje zgodnie z komenda
    if ruch == 'a':
        gracz_x = gracz_x - 1
    elif ruch == 's':
        gracz_y = gracz_y - 1
    elif ruch == 'd':
        gracz_x += 1
    elif ruch == 'w':
        gracz_y += 1
    else:
    print("Trzymaj sie regul")