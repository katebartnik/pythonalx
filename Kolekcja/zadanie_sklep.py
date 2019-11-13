"""
Oferujemy produkty

marchew: 2.35, ziemniaki: 2.2, cebula: 1.8, ogorki: 4.0

Co chcesz kupic?
Ile chcesz kupic?
za marchew płacisz:

"""

produkty = {"marchew" : 2.35,
            "ziemniaki" : 2.2,
            "cebula" : 1.8,
            "ogorki" : 4.0,
}

stan = { "marchew" : 100,
         "ziemniaki" : 10,
         "cebula" : 10,
         "ogorki" : 10,
}
print( """
Witaj w naszym zieleniaku
Wybierz z podanych produktów towar

""")

for produkt in produkty:
    print(f"- {produkt} : {produkty[produkt]} || Stan na magazynie - {stan}")

while True:
    tryb = input("Wybierz tryb : [z-zakupowy] [m-magazynowy] [k-konczymy]")
    if tryb == 'k':
        break
    elif tryb == 'z':
        while True:
            co_kupic = input("Co chcesz kupić?[wpisz k aby zakończyć] ")
            if co_kupic.lower() == 'k':
                break
            if co_kupic in produkty:
                ile = input(f"Ile chcesz kupić? [{co_kupic}] ")
                ile = float(ile)
            if ile < stan[co_kupic]:
                naleznosc = ile * produkty[co_kupic]
                stan[co_kupic] = stan[co_kupic] - ile
                print(f"Za [{co_kupic}] płacisz: {naleznosc:.2f} PLN")
            else:
                print("Ma za malo towaru ")
        else:
            print("Nie ma takiego produkty: ")
        while True:
            produkt_do_dodania = input("Co chcesz dodac: ")
            ile_do_dodania = input("Ile chcesz dodac: ")
            if not produkt_do_dodania in towary:
                cena_nowego_pr = float(input("Jaka będzie cena?: "))
                towary[produkt_do_dodania] = cena_nowego_pr
            stan = [produkt_do_dodania] = stan.get(produkt_do_dodania, 0) + ile_do_dodania


#zoptymalizować kod
