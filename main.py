import random

MAX_DIM = 15

def dobre_wymiary(n, m):
    if n < 2 or n > MAX_DIM or m < 2 or m > MAX_DIM:
        return False, "Niewlasciwy rozmiar! - musi miescic się w zakresie [2 - {}]".format(MAX_DIM)
    else:
        return True, ""

def dobre_miny(l_min, n, m):
    if l_min < 0 or l_min >= n*m:
        return False, "Niewlasciwa liczba min - musi byc nieujemna i mniejsza od {}".format(n*m)
    else:
        return True, ""

def pobierz_dane():
    "Pobieranie obu wymiarów planszy i liczby min od użytkownika"

    wymiary = input("Wprowadź oba wymiary planszy oddzielone spacją: ").split()
    n = int(wymiary[0])
    m = int(wymiary[1])
    while not dobre_wymiary(n, m)[0]:
        print(dobre_wymiary(n, m)[1])
        wymiary = input("Wprowadź oba wymiary planszy oddzielone spacją: ").split()
        n = int(wymiary[0])
        m = int(wymiary[1])

    l_min = int(input("Wprowadź liczbę min: "))
    while not dobre_miny(l_min, n, m)[0]:
        print(dobre_miny(l_min, n, m)[1])
        l_min = int(input("Wprowadź liczbę min: "))

    return n, m, l_min


class Przycisk: # Pole
    def __init__(self):
        self.bomba = False
        self.sasiednie_bomby = 0
        self.flaga = False
        self.pytajnik = False
        self.widoczny = False

    def pokaz(self):
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
    def __init__(self, n, m):
        self.tab_przyciskow = [[Przycisk() for i in range(m)] for j in range(n)]
        self.n = n
        self.m = m

    def kliknij(self):
        """Pobiera od użytkownika i zwraca tryb i wspolrzedne pola"""
        odczyt = input().split()
        tryb = odczyt[0]
        wspolrzedne = int(odczyt[1]), int(odczyt[2])
        return tryb, wspolrzedne

    def rozstaw_miny(self, l_min, x, y):
        """Wylosowanie pozycji i rozstawienie na nich bomb"""
        poz_pierwsza = x*self.m + y
        pozycje_do_losowania = list(range(self.n*self.m))
        pozycje_do_losowania.remove(poz_pierwsza) # usunięcie pierwszej zaznaczonej pozycji
        # print(pozycje_do_losowania)
        bombowa_lista = random.sample(pozycje_do_losowania, l_min)
        bombowa_lista_wspolrzedne = [(bombowa_lista[i]//self.m, bombowa_lista[i]%self.m) for i in range(l_min)]
        # print(bombowa_lista)
        print(bombowa_lista_wspolrzedne)
        for i, j in bombowa_lista_wspolrzedne:
            self.tab_przyciskow[i][j].bomba = True # ustawia dane pole na bombę
            # a następnie dla każdego pola dookoła niego zwiększa o 1 licznik sąsiednich bomb
            for k in [i-1, i, i+1]:
                for l in [j-1, j, j+1]:
                    if k >= 0 and k < self.n and l >= 0 and l < self.m: # przy zapewnieniu że pole istnieje
                        self.tab_przyciskow[k][l].sasiednie_bomby += 1

    def wyswietl(self):
        """Wyswietla aktualną planszę"""""
        print("|{0:4}||".format(''),end='')
        for i in range(self.m):
            print("{0:4}|".format(i),end='') # Górny, poziomy rząd kolejnych liczb opisujący 2. współrzędną pola
        print("\n","="*(6*self.m))
        for j in range(self.n):
            print("|{0:4}||".format(j),end='') # Boczny, pionowy rząd kolejnych liczb opisujący 1. współrzędną pola
            for k in range(self.m):
                wyswietlane_pole = self.tab_przyciskow[j][k]
                wyswietlane_pole.pokaz()
            print("\n",'-'*(6*self.m))

    def rozprzestrzeniaj(self, x, y):
        """funkcja rozprzestrzeniająca widoczność pól dookoła pola niesąsiadującego z minami"""
        for i in [x - 1, x, x + 1]:
            for j in [y - 1, y, y + 1]:
                if i >= 0 and j >= 0 and i < self.n and j < self.m: # jeśli dane pole istnieje (tzn ma odpowiednie współrzędne)
                    if not self.tab_przyciskow[i][j].widoczny: # jeśli pole niewidoczne to
                        self.tab_przyciskow[i][j].widoczny = True # ustawia na widoczne
                        if self.tab_przyciskow[i][j].sasiednie_bomby == 0: # sprawdza czy sąsiaduje z bombami i jeśli nie, to
                            self.rozprzestrzeniaj(i, j) # rozprzestrzenia się dalej

KLIK, FLAGA, PYTAJNIK = 'k', 'f', 'p'

def main():
    n, m, l_min = pobierz_dane()

    l_flag = 0
    l_pozostalych_min = l_min
    # napis = 'ROZPOCZNIJ GRĘ'
    # print(napis)
    # przycisk rozpoczęcia nowej gry(element interfejsu, z powyższym napisem
    nowa_plansza = Plansza(n, m)
    rozstawione = False
    print("WERJA WSTĘPNA (BEZ GUI):")
    print("Aby wywołać interakcję z danym polem należy wprowadzić polecenie według schematu:")
    print("<tryb> <1. wspolrzedna> <2. wspolrzedna>")
    print("Przykłady:\nk 2 3 - kliknięcie na pole o współrzędnych (2,3)")
    print("f 1 4 - oflagowanie (lub jego cofnięcie) pola o współrzędnych (1,4)")
    print("p 0 4 - oznaczenie (lub jego cofnięcie) znakiem zapytania pola o wspolrzednych (0,4)")

    while True:  # GŁÓWNA PĘTLA GRY
        print("="*80)
        print('SAPER'.center(80))
        print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(l_flag, l_pozostalych_min))
        tryb, wspolrzedne = nowa_plansza.kliknij()
        wskazane_pole = nowa_plansza.tab_przyciskow[wspolrzedne[0]][wspolrzedne[1]]
        if tryb == KLIK:  # kliknięcie na konkretne pole
            if not rozstawione:  # jeśli to pierwsze naciśnięte pole to rozstaw na reszcie pól planszy bomby
                nowa_plansza.rozstaw_miny(l_min, *wspolrzedne)
                rozstawione = True

            wskazane_pole.widoczny = True
            if wskazane_pole.sasiednie_bomby == 0:
                nowa_plansza.rozprzestrzeniaj(*wspolrzedne)

            if wskazane_pole.bomba:  # Jeśli w polu jest bomba:
                nowa_plansza.wyswietl()
                print("BOMBA - PRZEGRANA!")
                break

        if tryb == FLAGA:  # ustawienie lub usunięcie flagi na polu
            wskazane_pole.flaga = not wskazane_pole.flaga
            if wskazane_pole.flaga:
                l_flag += 1
                l_pozostalych_min -= 1
            else:
                l_flag -= 1
                l_pozostalych_min += 1
            wskazane_pole.pytajnik = False
        if tryb == PYTAJNIK:  # ustawienie lub usunięcie znaku zapytania
            wskazane_pole.pytajnik = not wskazane_pole.pytajnik
            wskazane_pole.flaga = False

        nowa_plansza.wyswietl()

        # SPRAWDZANIE, CZY WYGRANA
        licznik_odkrytych = 0
        wszystko_dobrze_oznaczone = True

        for rzad in nowa_plansza.tab_przyciskow:
            for pole in rzad:
                licznik_odkrytych += pole.widoczny
                if wszystko_dobrze_oznaczone and pole.bomba != pole.flaga:
                    wszystko_dobrze_oznaczone = False

        if licznik_odkrytych == n * m - l_min or wszystko_dobrze_oznaczone:
            print("GRATULACJE - WYGRAŁEŚ!")
            break


if __name__ == '__main__':
    main()


