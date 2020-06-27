"""Testy modułu main."""

import unittest
import main
import random
import dosymulacji
import time

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


class SymulacjaTest(unittest.TestCase):
    def setUp(self):
        self.n = 8
        self.m = 8
        self.l_min = 12

    def test_pierwsze_bez_bomby(self):
        """Wykonanie 10 testów z kliknięciem dowolnego pola w nowej grze, każde takie pole powinno być wolne od miny."""
        tryb = 'k'
        przypadkowe_pola = [(random.randrange(self.n), random.randrange(self.m)) for i in range(10)]
        for x, y in przypadkowe_pola:
            nowa_plansza = main.Plansza(self.n, self.m, self.l_min)
            byla_bomba = nowa_plansza.interakcja(tryb, x, y)
            self.assertFalse(byla_bomba)

    def test_symulacja_gry(self):
        nowa_plansza = main.Plansza(self.n, self.m, self.l_min)
        random.seed(1111)
        print("=" * 80)
        print('SAPER'.center(80))
        nowa_plansza.wyswietl()
        for tryb, x, y in dosymulacji.polecenia:
            print("=" * 80)
            print('SAPER'.center(80))
            print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(nowa_plansza.l_flag, nowa_plansza.l_pozostalych_min))
            print("\nUŻYTKOWNIK WPROWADZIŁ: {} {} {}\n".format(tryb, x, y))
            nowa_plansza.pojedynczy_ruch(tryb, x, y)
            time.sleep(1.0)

if __name__ == '__main__':
    unittest.main()