# napisz skrypt w ktorym przyjmiesz z konsoli info o sciezce z której chccesz wyszukać pliki i foldery
# wypisz je na konsoli i oznacz które to są pliki a które to foldery

import os #info o funkcjach umożliwiających pozyskiwanie informacji na temat plików i folderów znajdujących się na dysku twardym komputera a także tworzenie i usuwanie tychże plików.
import time

Path = input("Podaj ścieżkę: ")
ListedFiles = os.listdir(Path)

for item in ListedFiles:                        #aktualny katalog w którym jesteśmy
    if os.path.isfile(Path + item):                        #jesli to jest plik to true
        print("{} jest plikiem".format(item))

    if os.path.isdir(Path + item):
        print("{} jest folderem".format(item))