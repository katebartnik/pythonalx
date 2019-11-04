import unittest
class TestCzyPierwsza(unittest.TestCase):
    def test_czy_pierwsza_dla_liczby_pierwszej(self):
        self.assertEqual(cz_pierwsza(7), True)
        self.assertEqual(cz_pierwsza(11), True)
        self.assertEqual(cz_pierwsza(17), True)

    def test_czy_pierwsza_dla_liczby_niepierwszej(self):
        self.assertIs(cz_pierwsza(10), False)
        self.assertIs(cz_pierwsza(366), False)