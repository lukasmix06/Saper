"""Testy modułu main."""

import unittest

import main

class FalseInputTest(unittest.TestCase):
    """TEST 1 - Próba rozpoczęcia gry z niepoprawnym rozmiarem planszy i niepoprawną liczbą min"""

    def setUp(self):
        self.zle_wymiary = [(1, 1), (5, 1), (4, 1), (20, 500)]
        self.dobre_wymiary = [(5, 6), (3, 3), (8, 8)]
        self.zle_miny = [(-4, (5, 6)), (20, (3, 3)), (16, (4, 4))]
        self.dobre_miny = [(12, (8, 8)), (5, (5, 5))]

    def test_wymiary(self):
        for przyklad in self.zle_wymiary:
            self.assertEqual(main.dobre_wymiary(*przyklad)[1],
                             "Niewlasciwy rozmiar! - musi miescic się w zakresie [2 - {}]".format(main.MAX_DIM))

        for przyklad in self.dobre_wymiary:
            self.assertEqual(main.dobre_wymiary(*przyklad)[1],"")

    def test_bomby(self):
        for miny, rozmiar in self.zle_miny:
            self.assertEqual(main.dobre_miny(miny, *rozmiar)[1],
                            "Niewlasciwa liczba min - musi byc nieujemna i mniejsza od {}".format(rozmiar[0]*rozmiar[1]))
        for miny, rozmiar in self.dobre_miny:
            self.assertEqual(main.dobre_miny(miny, *rozmiar)[1],"")

if __name__ == '__main__':
    unittest.main()