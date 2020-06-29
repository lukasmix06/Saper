"""Testy modułu main."""

import unittest

import random

import main

import dosymulacji as ds


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
                             "Niewlasciwe rozmiary! - muszą miescic się w zakresie [2 - 15]".format(main.MAX_DIM))

        for przyklad in self.dobre_wymiary:
            self.assertEqual(main.dobre_wymiary(*przyklad)[1], "")

    def test_bomby(self):
        for miny, rozmiar in self.zle_miny:
            self.assertEqual(main.dobre_miny(miny, *rozmiar)[1],
                             "Niewlasciwa liczba min - musi byc nieujemna i mniejsza od {}".format(rozmiar[0]*rozmiar[1]))
        for miny, rozmiar in self.dobre_miny:
            self.assertEqual(main.dobre_miny(miny, *rozmiar)[1], "")


class RozgrywkaTest(unittest.TestCase):
    def setUp(self):
        self.dlugosc = 8
        self.szerokosc = 8
        self.liczba_min = 12
        self.nowa_plansza = main.Plansza(self.dlugosc, self.szerokosc, self.liczba_min)

    def test_pierwsze_bez_bomby(self):
        """Wykonanie 10 testów z kliknięciem dowolnego pola w nowej grze, każde takie pole powinno być wolne od miny."""
        tryb = 'k'
        przypadkowe_pola = [(random.randrange(self.dlugosc), random.randrange(self.szerokosc)) for i in range(10)]
        for x, y in przypadkowe_pola:
            nowa_plansza = main.Plansza(self.dlugosc, self.szerokosc, self.liczba_min)
            byla_bomba = nowa_plansza.interakcja(tryb, x, y)
            self.assertFalse(byla_bomba)

    def test_wygrana(self):
        """TEST 2. - Kliknięcie pola, wyświetla się liczba min w sąsiedztwie pola

       TEST 4. - Kliknięcie pola gdy brak min w sąsiedztwie

        TEST 5. - Oznaczenie pola jako “tu jest mina” - licznik oznaczonych powinien wzrosnąć o 1"""
        random.seed(1111)
        self.nowa_plansza.wyswietl()
        ostatnie_polecenie = ds.polecenia.pop()
        for tryb, x, y in ds.polecenia:
            self.assertFalse(self.nowa_plansza.pojedynczy_ruch(tryb, x, y))
        self.assertTrue(self.nowa_plansza.pojedynczy_ruch(*ostatnie_polecenie))

    def test_przegrana(self):
        """TEST 3. - Kliknięcie pola, wyświetla się mina, gra się kończy,"""
        random.seed(2222)
        self.nowa_plansza.wyswietl()
        ostanie_polecenie = ds.polecenia2.pop()
        for tryb, x, y in ds.polecenia2:
            self.assertFalse(self.nowa_plansza.pojedynczy_ruch(tryb, x, y))
        self.assertTrue(self.nowa_plansza.pojedynczy_ruch(*ostanie_polecenie))

    def test_znak_zapytania(self):
        """TEST 6. Oznaczenie pola jako “tu może być mina”"""
        for tryb, x, y in ds.polecenia3:
            self.nowa_plansza.interakcja(tryb, x, y)
        for i in range(self.dlugosc):
            for j in range(self.szerokosc):
                if (i, j) == (5, 3):
                    self.assertTrue(self.nowa_plansza.tab_przyciskow[i][j].pytajnik)
                elif (i, j) == (3, 5):
                    self.assertTrue(self.nowa_plansza.tab_przyciskow[i][j].pytajnik)
                else:
                    self.assertFalse(self.nowa_plansza.tab_przyciskow[i][j].pytajnik)


if __name__ == '__main__':
    unittest.main()
