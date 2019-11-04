#Napisz funkcje która s[rawdzi czy podana liczba jest liczba pierwsza

def czy_pierwsza(x):
    """
    SPrawdza czy x jest liczba pierwsza
    >>> czy_pierwsza(10)
    True
    >>>czy_pierwsza(7)
    True
    :param x:
    :return:
    """
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

assert czy_pierwsza(2) is True
assert czy_pierwsza(11) is True
assert czy_pierwsza(10) is False

#zapisywanie dokumentacji, doctest

print(help(czy_pierwsza()))