"""
Tworzenie rekordu pracownika
2 parametry obowiązkowe, 2 parametry opcjonalne #wartośc domyślna email = "emial@firma.pl"
Ma zwrócić zmienna typu slownik
"""
def utworz_pracownika(imie, nazwisko, email="info@firma.pl", telefon=None):
    pracownik = dict()
    pracownik["imie"] = imie
    pracownik["nazwisko"] = nazwisko
    pracownik["email"] = email
    pracownik["telefon"] = telefon
    return pracownik

print(utworz_pracownika("Jan", "Kowalski"))
print(utworz_pracownika("Adam", "Nowak", "anowak@firma.pl", "501111111"))
print(utworz_pracownika("Jan", "Zielinski", telefon="504444444"))
print(utworz_pracownika("Jan", "Zielinski", email="jzielinski@firma.pl"))
print(utworz_pracownika("Jan", "Zielinski", "jzielinski@firma.pl"))
