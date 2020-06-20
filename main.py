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
        czybomba = True


