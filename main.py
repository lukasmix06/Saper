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
        self.sasiednie_bomby = 0 #trzeba to jakoś zliczać, jeszcze nie wiem czy to ma być na poziomie przycisku czy planszy
        self.flaga = False
        self.pytajnik = False
        self.widoczny = False #nie wiem czy to w ogóle jest potrzebne

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
        print(pozycje_do_losowania)
        bombowa_lista = random.sample(pozycje_do_losowania, l_min)
        bombowa_lista_wspolrzedne = [(bombowa_lista[i]//m, bombowa_lista[i]%m) for i in range(l_min)]
        print(bombowa_lista)
        print(bombowa_lista_wspolrzedne)
        for i, j in bombowa_lista_wspolrzedne:
            self.tab_przyciskow[i][j].bomba = True

l_flag = 0
l_pozostalych_min = l_min
#napis = 'ROZPOCZNIJ GRĘ'
print('Rozpocznij grę')
#przycisk rozpoczęcia nowej gry(element interfejsu, z napisem string "Rozpocznij!")
nowa_plansza = Plansza(n, m)
rozstawione = 0

while 1: #PĘTLA GRY
    print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(l_flag, l_pozostalych_min))
    tryb, wspolrzedne = nowa_plansza.kliknij()
    wskazane_pole = Plansza.tab_przyciskow[wspolrzedne[0]][wspolrzedne[1]]
    if tryb == 'k' #kliknięcie na konkretne pole
        if rozstawione == 0: #jeśli to pierwsze naciśnięte pole to rozstaw na reszcie pól planszy bomby
            nowa_plansza.rozstaw_miny(l_min, *wspolrzedne)
            rozstawione = 1
        if wskazane_pole.bomba == True: #Jeśli w polu jest bomba:
            print(BOMBA - PRZEGRANA!)
            break
        else: #Jeśli w polu nie ma bomby:
            wskazane_pole.widoczne = True
    if tryb == 'f': #ustawienie flagi na polu
        wskazane_pole.flaga = True
        l_flag += 1
        l_pozostalych_min -= 1
    if tryb == 'p' #ustawienie znaku zapytania
    break



