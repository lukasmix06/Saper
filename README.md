# Saper
Projekt gry komputerowej Saper

* **Główne okno** gry będzie posiadać:
  * dwa pola tekstowe do wprowadzania przez użytkownika obu rozmiarów planszy - N na M pól
  * pole tekstowe dla wprowadzenia liczby min na planszy
  * pola tekstowe wyświetlające liczę oznaczonych dotąd pól jako miny oraz liczbę pozostałych min na planszy
  * przycisk rozpoczęcia nowej gry
  * wygenerowana graficzna siatka przycisków, będąca klasą, o wymiarach podanych przez użytkownika oraz liczbie ukrytych min zgodną z tą
  podaną przez użytkownika
  
  <UŻYWANE TYPY DANYCH, KLASY>
  
* **Komunikaty o błędach** pojawiają się podczas następujących akcji:
  * wprowadzany rozmiar planszy < 2 x 2 pola
  * wprowadzany rozmiar planszy > 15 x 15 pól
  * wprowadzenie ujemnej liczby min
  * wprowadzenie min większej niż wynikającej z rozmiarów planszy (m*n)
  
* **Sprawdzanie poprawności wprowadzanych danych** będzie odbywać się przy pomocy mechanizmu wyjątków np....

* Na początku gry na losowych wygenerowanych polach umieszczane są miny w liczbie zgodnej z podaną przez użytkowania, każde rozłożenie min jest równie prawdopodobne przy czym:
  * pierwsze pole na które kliknie użytkownik, nie może posiadać miny, w tym celu:
  - jeśli było ono wolne od miny nic się nie dzieje
  - nawet jeśli miało pierwotnie podłożoną minę, zachowuje się tak jakby jej nie miało, a jego mina zostaje przeniesiona na dowolne losowe pole wolne
  
  

