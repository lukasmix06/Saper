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

l_flag = 0
l_pozostalych_min = l_min
while 1:
    print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(l_flag, l_pozostalych_min))
    napis = 'Rozpocznij grę'
    break
    #przycisk rozpoczęcia nowej gry(element interfejsu, z napisem string "Rozpocznij!")

class Przycisk:
    def __init__(self):
        self.bomba = False
        self.sasiednie_bomby = 0 #trzeba to jakoś zliczać, jeszcze nie wiem czy to ma być na poziomie przycisku czy planszy
        self.flaga = False
        self.pytajnik = False
        self.zaznaczony = False #nie wiem czy to w ogóle jest potrzebne

class Plansza:
    def __init__(self, n, m):
        self.tab_przyciskow = [[Przycisk() for i in range(n)] for j in range(m)]

    def kliknij(self, x, y): #x i y to położenie przycisku
        pass

    def rozstaw_miny(self, l_min, x, y):
        poz_pierwsza = x + y #Źle to jest - poprawić!!!
        lista_bez_pierwszej = list(range((n*m)-1)).remove(poz_pierwsza)
        bombowa_lista = random.sample(lista_bez_pierwszej, l_min)
        bombowa_lista_wspolrzedne = [(bombowa_lista[i]//m, bombowa_lista[i]%m) for i in range(l_min)]
        for i, j in bombowa_lista_wspolrzedne:
            self.tab_przyciskow[i][j].bomba = True

while 1: #PĘTLA GRY
    #napis = 'Rozpocznij grę'
    #przycisk rozpoczęcia nowej gry(element interfejsu, z napisem string "Rozpocznij!")
    nowa_plansza = Plansza(n, m)
    nowa_plansza.kliknij(4, 4)
    nowa_plansza.rozstaw_miny(l_min, 4, 4)
    print("liczba oznaczonych pól: {}\nliczba pozostałych min: {}".format(l_flag, l_pozostalych_min))
    break



