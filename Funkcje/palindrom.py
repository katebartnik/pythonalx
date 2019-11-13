#Napisz funkcje ktora sprawdzi czy dany napis jest palindronem

#czy jest taki sam czytany wstecz


def is_palindrom(text):
    text = text.lower().replace(" ", "").replace(",", "")


    return text == text[::-1]
    #     return True
    # return False

def test_is_palindrom_for_palindrom():
    assert is_palindrom("kajak") is True
    assert is_palindrom("A to idiota") is True
    assert is_palindrom("A to idiota.") is True
    assert is_palindrom("Ada, gmina za nim gada.") is True

print(is_palindrom())
