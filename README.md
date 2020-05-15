# Saper
Projekt gry komputerowej Saper

* **Główne okno** gry będzie posiadać:
  * dwa pola tekstowe do wprowadzania przez użytkownika obu rozmiarów planszy - N na M pól (obie zmienne typ int)
  * pole tekstowe dla wprowadzenia liczby min na planszy (zmienna typ int)
  * pola tekstowe wyświetlające liczbę oznaczonych dotąd pól jako miny oraz liczbę pozostałych min na planszy (zmienne typ int)
  * przycisk rozpoczęcia nowej gry (element interfejsu, z napisem string "Rozpocznij!")
  * wygenerowana graficzna siatka przycisków o wymiarach podanych przez użytkownika oraz liczbie ukrytych min zgodną z tą
  podaną przez użytkownika
   - siatka będzie reprezentowana przez klasę, zawierającą tablicę 2 wymiarową obiektów-przycisków
  
  <UŻYWANE TYPY DANYCH, KLASY>
  
* **Komunikaty o błędach** pojawiają się podczas następujących akcji:
  * wprowadzany rozmiar planszy < 2 x 2 pola
  * wprowadzany rozmiar planszy > 15 x 15 pól
  * wprowadzenie ujemnej liczby min
  * wprowadzenie min większej niż wynikającej z rozmiarów planszy (m*n)
  
* **Sprawdzanie poprawności wprowadzanych danych** będzie odbywać się przy pomocy mechanizmu wyjątków np....

* **Na początku gry** na losowych wygenerowanych polach umieszczane są miny w liczbie zgodnej z podaną przez użytkowania, każde rozłożenie min jest równie prawdopodobne przy czym:
  * **pierwsze pole na które kliknie użytkownik**, nie może posiadać miny, w tym celu:
  - jeśli było ono wolne od miny nic się nie dzieje
  - nawet jeśli miało pierwotnie podłożoną minę, zachowuje się tak jakby jej nie miało, a jego mina zostaje przeniesiona na losowe pole wolne
  
**Po kliknięciu lewym przyciskiem** na pole:
 * jeśli jest tam mina, wyświetla się informacja o przegranej, gra się kończy
 * jeśli nie ma miny, ale w sąsiedztwie pola są miny, to pole dezaktywuje się, a na odkrytym przycisku wyświetlana jest ich liczba
 * jeśli nie ma miny i w bezpośrednim sąsiedztwie też nie ma miny, to to pole, dezaktywuje się, a wraz z nim dezaktywują się wszystkie sąsiadujące pola bez min, aż do pól, które z minami sąsiadują
 
**Po kliknięciu prawym przyciskiem** na pole:
 * można oflagować pole jako posiadające minę
 * po ponownym kliknięciu można oznakować pole znakiem zapytania, jako możliwa mina
 * po kolejnym kliknięciu oznaczenie znika
 
**Gra kończy się wygraną** w momencie:
 * gdy kliknięte zostaną wszystkie pola bez min lub
 * gdy oflagowane zostaną wszystkie, i jako jedyne, pola z minami
 
 **Tajemniczy manewr**:
 * Sekwencja klawiszy "xyzzy" pozwala na przyciemnienie pól pod którymi znajdują się miny.
 
 
 



 
  
  

