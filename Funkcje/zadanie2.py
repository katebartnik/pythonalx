"""
Napisz funkcje zwracajaca zbior wszystkich znaków wystepujacyhc w zadanym napisie wiecej niz podana liczba razy

>>wiecej_niz("ala ma kota a kot ma ale", 3)
#('a', ' ')

"""


def wiecej_niz(text, b):
    result = set()
    for s in set(text):
        if text.count(s) > b:
            result.add(s)
    return result


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set() #nie{}

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaa", 2) == {"a"}
