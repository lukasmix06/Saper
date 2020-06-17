while(1):
    n = int(input("Wprowadź pierwszy wymiar planszy: 5"))
    if n >= 2 and n <= 15:
        break
    else:
        print("Niewlasciwy rozmiar! - musi miescic się w zakresie [2 - 15]")

while(1):
    m = int(input("Wprowadź drugi wymiar planszy: "))
    if m >= 2 and m <= 15:
        break
    else:
        print("Niewlasciwy rozmiar! - musi miescic się w zakresie [2 - 15]")

while(1):
    lMin = int(input("Wprowadź liczbę min: "))
    if lMin >= 0 and lMin < n*m:
        break
    else:
        print("Niewlasciwa liczba min - musi byc nieujemna i mniejsza od calkowitej liczby pol")

