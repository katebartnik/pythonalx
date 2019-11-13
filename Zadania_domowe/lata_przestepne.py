"""
# Zainplementuj funkcję zwracającą listę lat przestępnych na podstawie zadanego zakresu

Lata przestepne(1990, 2020)
[1992, 1996, 2000, 2004, 2008]

rok przestepny jest co (4 lata, o ile nie dzieli się przez 100) albo dzieli się przez 400

"""

def test_lata_przestepne():
    assert lata_przestepne(2020, 2030) == [2020, 2024, 2028]
