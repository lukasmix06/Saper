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


class RozgrywkaTest(unittest.TestCase):
    def setUp(self):
        self.n = 8
        self.m = 8
        self.l_min = 12
        self.nowa_plansza = main.Plansza(self.n, self.m, self.l_min)

    def test_pierwsze_bez_bomby(self):
        """Wykonanie 10 testów z kliknięciem dowolnego pola w nowej grze, każde takie pole powinno być wolne od miny."""
        tryb = 'k'
        przypadkowe_pola = [(random.randrange(self.n), random.randrange(self.m)) for i in range(10)]
        for x, y in przypadkowe_pola:
            n_pl = main.Plansza(self.n, self.m, self.l_min)
            byla_bomba = n_pl.interakcja(tryb, x, y)
            self.assertFalse(byla_bomba)

    def test_symulacja_gry(self):
        """TEST 2. - Kliknięcie pola, wyświetla się liczba min w sąsiedztwie pola

       TEST 4. - Kliknięcie pola gdy brak min w sąsiedztwie

        TEST 5. - Oznaczenie pola jako “tu jest mina” - licznik oznaczonych powinien wzrosnąć o 1"""
        random.seed(1111)
        print("=" * 80)
        print('SAPER'.center(80))
        self.nowa_plansza.wyswietl()
        for tryb, x, y in dosymulacji.polecenia:
           print("=" * 80)
           print('SAPER'.center(80))
           print("\nUŻYTKOWNIK WPROWADZIŁ: {} {} {}\n".format(tryb, x, y))
           czy_koniec = self.nowa_plansza.pojedynczy_ruch(tryb, x, y)
           print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(self.nowa_plansza.l_flag,
                                                                                 self.nowa_plansza.l_pozostalych_min))
           time.sleep(1.0)
        self.assertTrue(czy_koniec)

    def test_przegrana(self):
        "TEST 3. - Kliknięcie pola, wyświetla się mina, gra się kończy,"
        time.sleep(3.0)
        random.seed(2222)
        print("=" * 80)
        print('SAPER'.center(80))
        self.nowa_plansza.wyswietl()
        for tryb, x, y in dosymulacji.polecenia2:
            print("=" * 80)
            print('SAPER'.center(80))
            print("\nUŻYTKOWNIK WPROWADZIŁ: {} {} {}\n".format(tryb, x, y))
            czy_koniec = self.nowa_plansza.pojedynczy_ruch(tryb, x, y)
            print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(self.nowa_plansza.l_flag,
                                                                                  self.nowa_plansza.l_pozostalych_min))
            time.sleep(1.0)
        self.assertTrue(czy_koniec)
        time.sleep(3.0)

    def test_znak_zapytania(self):
        """TEST 6. Oznaczenie pola jako “tu może być mina”"""
        for tryb, x, y in dosymulacji.polecenia3:
            self.nowa_plansza.interakcja(tryb, x, y)
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) == (5, 3):
                    self.assertTrue(self.nowa_plansza.tab_przyciskow[i][j].pytajnik)
                elif (i, j) == (3, 5):
                    self.assertTrue(self.nowa_plansza.tab_przyciskow[i][j].pytajnik)
                else:
                    self.assertFalse(self.nowa_plansza.tab_przyciskow[i][j].pytajnik)




if __name__ == '__main__':
    unittest.main()