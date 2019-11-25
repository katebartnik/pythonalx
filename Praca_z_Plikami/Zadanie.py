"""
Napisz funkcję która otworzy podany jako argument plik (podana nazwa pliku lub ścieżka) i wypisze numerując linię
"""



def numerator():
    with open("test2", encoding='utf-8') as file:
        index = 1
        for line in file:
            print(str(index) + ' ' + line)
            index += 1


numerator()


#Jak dodać jakiś napis na konsoli za pomoca argv sys