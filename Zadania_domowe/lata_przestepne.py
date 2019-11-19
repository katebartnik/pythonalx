"""
# Zainplementuj funkcję zwracającą listę lat przestępnych na podstawie zadanego zakresu

Lata przestepne(1990, 2020)
[1992, 1996, 2000, 2004, 2008]

rok przestepny jest co (4 lata, o ile nie dzieli się przez 100) albo dzieli się przez 400

"""
excludedYears = [100, 200, 300]

def lata_przestepne(startYear, endYear):
    wynik = []
    for year in range(startYear, endYear):
        if year % 4 == 0 and year not in excludedYears:
            wynik.append(year)
    return wynik

def test_lata_przestepne():
    assert lata_przestepne(2020, 2030) == [2020, 2024, 2028]
    assert lata_przestepne(86, 102) == [88, 92, 96]



returnMetodElement = lata_przestepne(1800, 2100)
print(returnMetodElement)
