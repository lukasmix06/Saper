import random

while 1:
    n = int(input("Wprowadź pierwszy wymiar planszy: "))
    if n >= 2 and n <= 15:
        break
    else:
        print("Niewlasciwy rozmiar! - musi miescic się w zakresie [2 - 15]")

while 1:
    m = int(input("Wprowadź drugi wymiar planszy: "))
    if m >= 2 and m <= 15:
        break
    else:
        print("Niewlasciwy rozmiar! - musi miescic się w zakresie [2 - 15]")

while 1:
    l_min = int(input("Wprowadź liczbę min: "))
    if l_min >= 0 and l_min < n*m:
        break
    else:
        print("Niewlasciwa liczba min - musi byc nieujemna i mniejsza od calkowitej liczby pol")

class Przycisk:
    def __init__(self):
        self.bomba = False
        self.sasiednie_bomby = 0
        self.flaga = False
        self.pytajnik = False
        self.widoczny = False

class Plansza:
    def __init__(self, n, m):
        self.tab_przyciskow = [[Przycisk() for i in range(m)] for j in range(n)]

    def kliknij(self):
        odczyt = input().split()
        tryb = odczyt[0]
        wspolrzedne = int(odczyt[1]), int(odczyt[2])
        return tryb, wspolrzedne

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
        print("|{0:5}|".format(''),end='')
        for i in range(m):
            print("{0:5}|".format(i),end='') #GÓRNY RZĄD
        print("\n","-----"*(m+2))
        for j in range(n):
            print("|{0:5}|".format(j),end='')
            for k in range(m):
                wyswietlane_pole = self.tab_przyciskow[j][k]
                if wyswietlane_pole.widoczny:
                    if wyswietlane_pole.bomba:
                        print("{0:5}|".format('@'),end='')
                    else:
                        print("{0:5}|".format(wyswietlane_pole.sasiednie_bomby),end='')
                else:
                    if wyswietlane_pole.flaga:
                        print("{0:5}|".format('#'),end='')
                    elif wyswietlane_pole.pytajnik:
                        print("{0:5}|".format('?'), end='')
                    else:
                        print("{0:5}|".format(''), end='')
            print("\n",'-----'*(m+2))




l_flag = 0
l_pozostalych_min = l_min
#napis = 'ROZPOCZNIJ GRĘ'
print('Rozpocznij grę')
#przycisk rozpoczęcia nowej gry(element interfejsu, z napisem string "Rozpocznij!")
nowa_plansza = Plansza(n, m)
rozstawione = 0



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
    if tryb == 'p': #ustawienie lub usunięcie znaku zapytania
        wskazane_pole.pytajnik = not wskazane_pole.pytajnik

    nowa_plansza.wyswietl()




