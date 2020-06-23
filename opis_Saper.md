# Saper
Projekt gry komputerowej Saper

Repozytorium w GitHub: https://github.com/lukasmix06/Saper

* **Główne okno** gry będzie posiadać:
  * dwa pola tekstowe do wprowadzania przez użytkownika obu rozmiarów planszy - N na M pól (obie zmienne typ int)
  * pole tekstowe dla wprowadzenia liczby min na planszy (zmienna typ int)
  * pola tekstowe wyświetlające liczbę oznaczonych dotąd pól jako miny oraz liczbę pozostałych min na planszy (zmienne typ int)
  * przycisk rozpoczęcia nowej gry (element interfejsu, z napisem string "Rozpocznij!")
  * wygenerowana graficzna siatka przycisków o wymiarach podanych przez użytkownika oraz liczbie ukrytych min zgodną z tą
  podaną przez użytkownika
   - siatka będzie reprezentowana przez klasę, zawierającą tablicę 2 wymiarową obiektów-przycisków(pól), każde pole będzie posiadać co najmniej 5 zmiennych, z których:
    1. reprezentuje fakt posiadania bomby (1) lub jej braku (0)
    2. zmienna, która przechowuje zliczone bomby w sąsiednich polach
    3. zmienna odnotowująca fakt oflagowania (0 lub 1)
    4. zmienna odnotowująca oznaczenie pola znakiem zapytania (0 lub 1)
    5. fakt naciśnięcie danego pola - staje się ono widoczne (0 lub 1)
    
* **Komunikaty o błędach** pojawiają się podczas następujących akcji:
  * wprowadzany rozmiar planszy < 2 x 2 pola
  * wprowadzany rozmiar planszy > 15 x 15 pól
  * wprowadzenie ujemnej liczby min
  * wprowadzenie liczby min równej lub większej niż wynikającej z rozmiarów planszy (m*n)
  
* **Sprawdzanie poprawności wprowadzanych danych** będzie odbywać się przy pomocy mechanizmu wyjątków

* **Na początku gry** żadne z pól nie posiada bomby, przy założeniu że **pierwsze pole, na które kliknie użytkownik**, nie może posiadać miny, pozwalamy na kliknięcie dowolnego pola
przez użytkownika, a następnie na pozostałych polach rozmieszczamy losowo wygenerowane miny w liczbie zgodnej z podaną przez użytkownika.
  
* **Po kliknięciu lewym przyciskiem** na pole:
  * jeśli jest tam mina, wyświetla się informacja o przegranej, gra się kończy
  * jeśli nie ma miny, ale w sąsiedztwie pola są miny, to pole dezaktywuje się, a na odkrytym przycisku wyświetlana jest ich liczba
  * jeśli nie ma miny i w bezpośrednim sąsiedztwie też nie ma miny, to to pole, dezaktywuje się, a wraz z nim dezaktywują się wszystkie sąsiadujące pola bez min, aż do pól, które z minami sąsiadują
 
* **Po kliknięciu prawym przyciskiem** na pole:
  * można oflagować pole jako posiadające minę
  * po ponownym kliknięciu można oznakować pole znakiem zapytania, jako możliwa mina
  * po kolejnym kliknięciu oznaczenie znika
 
* **Gra kończy się wygraną** w momencie:
  * gdy kliknięte zostaną wszystkie pola bez min lub
  * gdy oflagowane zostaną wszystkie, i jako jedyne, pola z minami
 
* **Tajemny manewr**:
  * Sekwencja klawiszy "xyzzy" pozwala na przyciemnienie pól pod którymi znajdują się miny.
 
* **Testy**:
 1. Próba rozpoczęcia gry z rozmiarem planszy i liczbą min: (1 na 1; 1), (5 na 1; 2), (4 na 1; 2), (20 na 500; 12), (5 na 6; -4), (3 na 3; 10), (1 na 10; 5) - oczekiwane komunikaty o błędzie. Wprowadzenie rozmiarów planszy 8 na 8 i liczby min równej 12 na potrzeby kolejnych testów.
 2. Kliknięcie pola, wyświetla się liczba min w sąsiedztwie pola,
 3. Kliknięcie pola, wyświetla się mina, gra się kończy,
 4. Kliknięcie pola, brak min w sąsiedztwie - oczekiwane automatyczne sprawdzenie sąsiadów aż do wyznaczenia obszaru wyznaczonego przez pola sąsiadujące z minami lub krawędzie planszy,
  5. Oznaczenie pola jako “tu jest mina” - licznik oznaczonych powinien wzrosnąć o 1,
  6. Oznaczenie innego pola jako “tu może być mina”,
  7. Oznaczenie pola, odznaczenie go, ponowne oznaczenie i ponowne odznaczenie - licznik oznaczonych powinien się odpowiednio aktualizować,
  8. Wygranie gry przez kliknięcie wszystkich pól bez min,
  9. Wygranie gry przez oznaczenie wszystkich pól z minami
  10. Próba oznaczenia sprawdzonego pola - oczekiwane niepowodzenie,
  11. Sprawdzenie kilku pól bez min, oznaczenie pól “tu jest mina”, rozpoczęcie nowej gry - licznik min powinien się zaktualizować, a pola zresetować.
  12. Wpisanie kodu xyzzy, zresetowanie gry - wszystkie pola powinny odzyskać standardowy kolor.
  13. Wykonanie 10 testów z kliknięciem pierwszego dowolnie wybranego pola w nowej grze, każde takie pole powinno być wolne od miny.
 
 
 
 



 
  
  

