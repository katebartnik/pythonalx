# losowanie

import random
#print(dir(random))
#print(help(random.randint))

print(random.randint(1, 10))

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)


skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

print("Położenie gracza", gracz_x, gracz_x)
print("Położenie skarbu", skarb_x, skarb_y)

#max, mix

#zamiana ujemnej liczby na dodatnią
print(abs(100))
print(abs(-100))

odleglosc = abs(skarb_x-gracz_x) + abs(skarb_y-gracz_y)
print(odleglosc)


x = 1
warunek = x > 7
while x>7:
    print("jestem w pętli")

while False:
    print("Jestem w pętli")

x = 10
while x > 0:
    print(x)
    x = x - 1

while True:
    instrukcja = input("Wciśniej 'k' aby zakończyć")
    if instrukcja == 'k':
        break

x = 10
while x > 0:
    if x == 6:
        x -= 1
        continue
    print(x)
    x = x - 1