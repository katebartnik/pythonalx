import os

def item(Path):
    ListedFiles = os.listdir(Path)

    for item in ListedFiles:  # aktualny katalog w którym jesteśmy
        if os.path.isfile(Path + item):  # jesli to jest plik to true
            print("{} jest plikiem".format(item))

        if os.path.isdir(Path + item):
            print("{} jest folderem".format(item))

Path = input("Podaj ścieżkę: ")
item(Path)
