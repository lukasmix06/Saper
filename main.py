import random

MAX_DIM = 15
KLIK, FLAGA, PYTAJNIK = 'k', 'f', 'p'

def dobre_wymiary(dlugosc, szerokosc):
    """Funkcja pobiera dlugosc i szerokosc planszy, ocenia ich poprawność i wypisuje odpowiedni komunikat"""
    if not (1 < dlugosc <= MAX_DIM) or not (1 < szerokosc <= MAX_DIM):
        return False, "Niewlasciwe rozmiary! - muszą miescic się w zakresie [2 - {}]".format(MAX_DIM)
    else:
        return True, ""

def dobre_miny(liczba_min, dlugosc, szerokosc):
    """Funkcja pobiera liczbę min, ocenia jej poprawność i wypisuje odpowiedni komunikat"""
    if not (0 <= liczba_min < dlugosc*szerokosc):
        return False, "Niewlasciwa liczba min - musi byc nieujemna i mniejsza od {}".format(dlugosc*szerokosc)
    else:
        return True, ""

def pobierz_dane():
    """Pobieranie obu wymiarów planszy i liczby min od użytkownika"""

    wymiary = input("Wprowadź oba wymiary planszy oddzielone spacją: ").split()
    dlugosc = int(wymiary[0])
    szerokosc = int(wymiary[1])
    while not dobre_wymiary(dlugosc, szerokosc)[0]:
        print(dobre_wymiary(dlugosc, szerokosc)[1])
        wymiary = input("Wprowadź oba wymiary planszy oddzielone spacją: ").split()
        dlugosc = int(wymiary[0])
        szerokosc = int(wymiary[1])

    liczba_min = int(input("Wprowadź liczbę min: "))
    while not dobre_miny(liczba_min, dlugosc, szerokosc)[0]:
        print(dobre_miny(liczba_min, dlugosc, szerokosc)[1])
        liczba_min = int(input("Wprowadź liczbę min: "))

    return dlugosc, szerokosc, liczba_min


class Przycisk: # Pole
    def __init__(self):
        self.bomba = False
        self.sasiednie_bomby = 0
        self.flaga = False
        self.pytajnik = False
        self.widoczny = False

    def pokaz(self):
        """Metoda wyświetlająca konkretny pole (przycisk) zależnie od jego stanu"""
        if self.widoczny:
            if self.bomba:
                print("@|".rjust(5), end='')
            else:
                print("{0:4}|".format(self.sasiednie_bomby), end='')
        else:
            if self.flaga:
                print("#|".rjust(5), end='')
            elif self.pytajnik:
                print("?|".rjust(5), end='')
            else:
                print("|".rjust(5), end='')

class Plansza:
    def __init__(self, dlugosc, szerokosc, liczba_min):
        self.tab_przyciskow = [[Przycisk() for i in range(szerokosc)] for j in range(dlugosc)]
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
        self.liczba_flag = 0
        self.liczba_min = liczba_min
        self.liczba_pozostalych_min = liczba_min
        self.rozstawione = False

    def kliknij(self):
        """Pobiera od użytkownika i zwraca tryb i wspolrzedne pola"""
        odczyt = input().split()
        tryb = odczyt[0]
        x, y = int(odczyt[1]), int(odczyt[2])
        return tryb, x, y

    def rozstaw_miny(self, x, y):
        """Wylosowanie pozycji i rozstawienie na nich bomb"""
        pozycja_pierwsza = x*self.szerokosc + y
        pozycje_do_losowania = list(range(self.dlugosc*self.szerokosc))
        pozycje_do_losowania.remove(pozycja_pierwsza) # usunięcie pierwszej zaznaczonej pozycji
        # print(pozycje_do_losowania)
        bombowa_lista = random.sample(pozycje_do_losowania, self.liczba_min)
        bombowa_lista_wspolrzedne = [(bombowa_lista[i]//self.szerokosc, bombowa_lista[i]%self.szerokosc)
                                     for i in range(self.liczba_min)]
        # print(bombowa_lista)
        # print(bombowa_lista_wspolrzedne)
        for i, j in bombowa_lista_wspolrzedne:
            self.tab_przyciskow[i][j].bomba = True # ustawia dane pole na bombę
            # a następnie dla każdego pola dookoła niego zwiększa o 1 licznik sąsiednich bomb
            for k in [i-1, i, i+1]:
                for l in [j-1, j, j+1]:
                    if 0 <= k < self.dlugosc and 0 <= l < self.szerokosc: # przy zapewnieniu że pole istnieje
                        self.tab_przyciskow[k][l].sasiednie_bomby += 1

    def wyswietl(self):
        """Wyswietla aktualną planszę"""""
        print("|{0:4}||".format(''), end='')
        for i in range(self.szerokosc):
            print("{0:4}|".format(i), end='') # Górny, poziomy rząd kolejnych liczb opisujący 2. współrzędną pola
        print("\n", "="*(6*self.szerokosc))
        for j in range(self.dlugosc):
            print("|{0:4}||".format(j), end='') # Boczny, pionowy rząd kolejnych liczb opisujący 1. współrzędną pola
            for k in range(self.szerokosc):
                wyswietlane_pole = self.tab_przyciskow[j][k]
                wyswietlane_pole.pokaz()
            print("\n", '-'*(6*self.szerokosc))

    def rozprzestrzeniaj(self, x, y):
        """Metoda rozprzestrzeniająca widoczność pól dookoła pola niesąsiadującego z minami"""
        for i in [x - 1, x, x + 1]:
            for j in [y - 1, y, y + 1]:
                if 0 <= i < self.dlugosc and 0 <= j < self.szerokosc: # jeśli dane pole istnieje (tzn ma odpowiednie współrzędne)
                    if not self.tab_przyciskow[i][j].widoczny: # jeśli pole niewidoczne to
                        self.tab_przyciskow[i][j].widoczny = True # ustawia na widoczne
                        if self.tab_przyciskow[i][j].sasiednie_bomby == 0: # sprawdza czy sąsiaduje z bombami i jeśli nie, to
                            self.rozprzestrzeniaj(i, j) # rozprzestrzenia się dalej

    def interakcja(self, tryb, x, y):
        """Metoda pobiera tryb interakcji oraz wspolrzedne pola i przeprowadza na nim odpowiednią operację"""
        wskazane_pole = self.tab_przyciskow[x][y]
        if tryb == KLIK:  # kliknięcie na konkretne pole
            if not self.rozstawione:  # jeśli to pierwsze naciśnięte pole to rozstaw na reszcie pól planszy bomby
                self.rozstaw_miny(x, y)
                self.rozstawione = True

            wskazane_pole.widoczny = True
            if wskazane_pole.sasiednie_bomby == 0:
                self.rozprzestrzeniaj(x, y)

            if wskazane_pole.bomba:  # Jeśli w polu jest bomba:
                self.wyswietl()
                print("BOMBA - PRZEGRANA!")
                return True

        if tryb == FLAGA:  # ustawienie lub usunięcie flagi na polu
            wskazane_pole.flaga = not wskazane_pole.flaga
            if wskazane_pole.flaga:
                self.liczba_flag += 1
                self.liczba_pozostalych_min -= 1
            else:
                self.liczba_flag -= 1
                self.liczba_pozostalych_min += 1
            wskazane_pole.pytajnik = False
        if tryb == PYTAJNIK:  # ustawienie lub usunięcie znaku zapytania
            wskazane_pole.pytajnik = not wskazane_pole.pytajnik
            wskazane_pole.flaga = False
        return False




    def pojedynczy_ruch(self, tryb, x, y):
        """Metoda wykonująca operacje na planszy przy pojedynczym przejściu pętli takie jak:

        zmiana stanu wybranego pola na planszy, wyswietlenie zaktualilzowaanej planszy, kontrola wygranej

        zwraca informację o zakończeniu rozgrywki (gdy bomba lub wygrana)"""


        if self.interakcja(tryb, x, y):
            return True  # KONIEC GRY, BO BOMBA

        self.wyswietl()

        # SPRAWDZANIE, CZY WYGRANA
        licznik_odkrytych = 0
        wszystko_dobrze_oznaczone = True
        for rzad in self.tab_przyciskow:
            for pole in rzad:
                licznik_odkrytych += pole.widoczny
                if wszystko_dobrze_oznaczone and pole.bomba != pole.flaga:
                    wszystko_dobrze_oznaczone = False

        if licznik_odkrytych == self.dlugosc * self.szerokosc - self.liczba_min or wszystko_dobrze_oznaczone:
            print("GRATULACJE - WYGRAŁEŚ!")
            return True #KONIEC GRY, BO WYGRANA
        else:
            return False



def main():
    dlugosc, szerokosc, liczba_min = pobierz_dane()

    # napis = 'ROZPOCZNIJ GRĘ'
    # print(napis)
    # przycisk rozpoczęcia nowej gry(element interfejsu, z powyższym napisem

    nowa_plansza = Plansza(dlugosc, szerokosc, liczba_min)

    print("WERJA WSTĘPNA (BEZ GUI):")
    print("Aby wywołać interakcję z danym polem należy wprowadzić polecenie według schematu:")
    print("<tryb> <1. wspolrzedna> <2. wspolrzedna>")
    print("Przykłady:\nk 2 3 - kliknięcie na pole o współrzędnych (2, 3)")
    print("f 1 4 - oflagowanie (lub jego cofnięcie) pola o współrzędnych (1, 4)")
    print("p 0 4 - oznaczenie (lub jego cofnięcie) znakiem zapytania pola o wspolrzednych (0, 4)")

    print("=" * 80)
    print('SAPER'.center(80))
    print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(nowa_plansza.liczba_flag,
                                                                          nowa_plansza.liczba_pozostalych_min))
    nowa_plansza.wyswietl()
    while True:  # GŁÓWNA PĘTLA GRY
        tryb, x, y = nowa_plansza.kliknij()
        print("=" * 80)
        print('SAPER'.center(80))
        print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(nowa_plansza.liczba_flag,
                                                                              nowa_plansza.liczba_pozostalych_min))

        if nowa_plansza.pojedynczy_ruch(tryb, x, y):
            break


if __name__ == '__main__':
    main()


