# Saper
Projekt gry komputerowej Saper

* **Główne okno** gry będzie posiadać:
  * dwa pola tekstowe do wprowadzania przez użytkownika obu rozmiarów planszy - N na M pól
  * pole tekstowe dla wprowadzenia liczby min na planszy
  * pola tekstowe wyświetlające liczę oznaczonych dotąd pól jako miny oraz liczbę pozostałych min na planszy
  * przycisk rozpoczęcia nowej gry
  * wygenerowana graficzna siatka przycisków o wymiarach podanych przez użytkownika oraz liczbie ukrytych min zgodną z tą
  podaną przez użytkownika
  
* **Komunikaty o błędach** pojawiają się podczas następujących akcji:
  * wprowadzenie rozmiwaru planszy miejszego od 2 x 2 pola
  * wprowadzenie rozmiaru planszy > od 15 x 15 pól
  * wprowadzenie ujemnej liczby min
  * wprowadzenie min większej niż wynikającej z rozmiarów planszy (m*n)
  
* **Sprawdzanie poprawności wprowadzanych danych** będzie odbywać się przy pomocy mechanizmu wyjątków np....

