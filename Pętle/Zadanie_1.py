#Zapytaj użytkowanika o 10 liczba i wypisz ich średnią
# Skorzystaj z petki for i range,

lista = list(range(10))
suma = 0

for x in lista:
    imputValue = int(input("Podaj wartość: "))
    suma += imputValue

print(suma)
print(suma/10)



