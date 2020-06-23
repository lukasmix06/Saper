import random
import exceptions

#import tkinter as tk

#okno = tk.Tk()

#etykieta = tk.Label(okno, "SAPER")

while 1:
    n = int(input("Wprowadź pierwszy wymiar planszy: "))
    try:
        if n < 2 or n > 15:
            raise exceptions.zły_wymiar()
    except exceptions.zły_wymiar:
        print("Niewlasciwy rozmiar! - musi miescic się w zakresie [2 - 15]")
    else:
        break

while 1:
    m = int(input("Wprowadź drugi wymiar planszy: "))
    try:
        if m < 2 or m > 15:
            raise exceptions.zły_wymiar()
    except exceptions.zły_wymiar:
        print("Niewlasciwy rozmiar! - musi miescic się w zakresie [2 - 15]")
    else:
        break


while 1:
    l_min = int(input("Wprowadź liczbę min: "))
    try:
        if l_min < 0 or l_min >= n*m:
            raise exceptions.zla_liczba_min()
    except exceptions.zla_liczba_min:
        print("Niewlasciwa liczba min - musi byc nieujemna i mniejsza od calkowitej liczby pol")
    else:
        break


class Przycisk: #Pole
    def __init__(self):
        self.bomba = False
        self.sasiednie_bomby = 0
        self.flaga = False
        self.pytajnik = False
        self.widoczny = False
        #self.tu_bylem = False #zmienna pomocnicza, zapobiegająca zapętlaniu w metodzie Planszy "rozprzestrzeniaj"

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

    def kliknij(self):
        odczyt = input().split()
        tryb = odczyt[0]
        wspolrzedne = int(odczyt[1]), int(odczyt[2])
        return tryb, wspolrzedne #zwraca pobrany z klawiatury tryb i współrzędne pola

    def rozstaw_miny(self, l_min, x, y):
        poz_pierwsza = x*m + y
        pozycje_do_losowania = list(range(n*m))
        pozycje_do_losowania.remove(poz_pierwsza) #usunięcie pierwszej zaznaczonej pozycji
        #print(pozycje_do_losowania)
        bombowa_lista = random.sample(pozycje_do_losowania, l_min)
        bombowa_lista_wspolrzedne = [(bombowa_lista[i]//m, bombowa_lista[i]%m) for i in range(l_min)]
        #print(bombowa_lista)
        print(bombowa_lista_wspolrzedne)
        for i, j in bombowa_lista_wspolrzedne:
            self.tab_przyciskow[i][j].bomba = True #ustawia dane pole na bombę
            # a następnie dla każdego pola dookoła niego zwiększa o 1 licznik sąsiednich bomb
            for k in [i-1, i, i+1]:
                for l in [j-1, j, j+1]:
                    if k >= 0 and k < n and l >= 0 and l < m: #przy zapewnieniu że pole istnieje
                        self.tab_przyciskow[k][l].sasiednie_bomby += 1

    def wyswietl(self):
        print("|{0:4}||".format(''),end='')
        for i in range(m):
            print("{0:4}|".format(i),end='') #Górny, poziomy rząd kolejnych liczb opisujący 2. współrzędną pola
        print("\n","="*(6*m))
        for j in range(n):
            print("|{0:4}||".format(j),end='') #Boczny, pionowy rząd kolejnych liczb opisujący 1. współrzędną pola
            for k in range(m):
                wyswietlane_pole = self.tab_przyciskow[j][k]
                wyswietlane_pole.pokaz()
            print("\n",'-'*(6*m))

    def rozprzestrzeniaj(self, x, y): #funkcja rozprzestrzeniająca widoczne pola, dookoła pola niesąsiadującego z minami
        for i in [x - 1, x, x + 1]:
            for j in [y - 1, y, y + 1]:
                if i >= 0 and j >= 0 and i < n and j < m: #jeśli dane pole istnieje (tzn ma odpowiednie współrzędne)
                    if self.tab_przyciskow[i][j].widoczny == 0: #jeśli pole niewidoczne to
                        self.tab_przyciskow[i][j].widoczny = 1 #ustawia na widoczne
                        if self.tab_przyciskow[i][j].sasiednie_bomby == 0: #sprawdza czy sąsiaduje z bombami i jeśli nie, to
                            self.rozprzestrzeniaj(i, j) #rozprzestrzenia się dalej


l_flag = 0
l_pozostalych_min = l_min
#napis = 'ROZPOCZNIJ GRĘ'
#print(napis)
#przycisk rozpoczęcia nowej gry(element interfejsu, z powyższym napisem
nowa_plansza = Plansza(n, m)
rozstawione = 0
print("WERJA WSTĘPNA (BEZ GUI):")
print("Aby wywołać interakcję z danym polem należy wprowadzić polecenie według schematu:")
print("<tryb> <1. wspolrzedna> <2. wspolrzedna>")
print("Przykłady:\nk 2 3 - kliknięcie na pole o współrzędnych (2,3)")
print("f 1 4 - oflagowanie (lub jego cofnięcie) pola o współrzędnych (1,4)")
print("p 0 4 - oznaczenie (lub jego cofnięcie) znakiem zapytania pola o wspolrzednych (0,4)")


while 1: #GŁÓWNA PĘTLA GRY
    print("=====================================================================================================================================")
    print('SAPER'.center(50))
    print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(l_flag, l_pozostalych_min))
    tryb, wspolrzedne = nowa_plansza.kliknij()
    wskazane_pole = nowa_plansza.tab_przyciskow[wspolrzedne[0]][wspolrzedne[1]]
    if tryb == 'k': #kliknięcie na konkretne pole
        if rozstawione == 0: #jeśli to pierwsze naciśnięte pole to rozstaw na reszcie pól planszy bomby
            nowa_plansza.rozstaw_miny(l_min, *wspolrzedne)
            rozstawione = 1

        wskazane_pole.widoczny = True
        if wskazane_pole.sasiednie_bomby == 0:
            nowa_plansza.rozprzestrzeniaj(*wspolrzedne)

        if wskazane_pole.bomba == True: #Jeśli w polu jest bomba:
            nowa_plansza.wyswietl()
            print("BOMBA - PRZEGRANA!")
            break

    if tryb == 'f': #ustawienie lub usunięcie flagi na polu
        wskazane_pole.flaga = not wskazane_pole.flaga
        if wskazane_pole.flaga == True:
            l_flag += 1
            l_pozostalych_min -= 1
        else:
            l_flag -= 1
            l_pozostalych_min += 1
        wskazane_pole.pytajnik = 0
    if tryb == 'p': #ustawienie lub usunięcie znaku zapytania
        wskazane_pole.pytajnik = not wskazane_pole.pytajnik
        wskazane_pole.flaga = 0

    nowa_plansza.wyswietl()

    wszystko_dobrze_oznaczone = 1
    for i in range(n):
        for j in range(m):
            if nowa_plansza.tab_przyciskow[i][j].bomba != nowa_plansza.tab_przyciskow[i][j].flaga:
                wszystko_dobrze_oznaczone = 0
                break

    licznik_odkrytych = sum([nowa_plansza.tab_przyciskow[i][j].widoczny for i in range(n) for j in range(m)])
    if licznik_odkrytych == n*m - l_min or wszystko_dobrze_oznaczone == 1:
        print("GRATULACJE - WYGRAŁEŚ!")
        break





