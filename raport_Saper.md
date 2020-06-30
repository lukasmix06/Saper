**SPRAWOZDANIE Z PROJEKTU - SAPER**

- Jest to wersja z podstawową grafiką utworzoną w wierszu poleceń w konsoli. 

- GŁÓWNE KLASY:
  - Główny rdzeń programu stanowi **klasa "Plansza"**, która zawiera wiele metod, na niej odbywa się większość operacji i przekształceń. Zawiera ona w sobie **obiekty klasy - "Przycisk"**, która reprezentuje pojedyncze pole na planszy. 
  - Każde takie pole zawiera szereg zmiennych opisujących jego stan m.in czy zawiera bombę **(bomba)**, czy jest oflagowane **("flaga")**, czy chociażby czy pole jest już widoczne dla użytkownika, tzn. czy zostało już przez niego kliknięte **("widoczny")**.

- OMÓWIENIE FUNKCJONALNOŚCI:
  - Na początku programu **użytkownik jest proszony o podanie obu wymiarów planszy**, aż do momentu gdy będą one spełniały odpowiednie kryteria wielkości. **(funkcja dobre_wymiary)**
  - Następnie **użytkownik podaje liczbę min**, która musi być mniejsza od liczby pól. **(funkcja dobre_miny)**.
  - Gdy program pobierze od użytownika potrzebne i prawidłowe dane przekazuje je do **nowotworzonego obietku planszy**. Podczas inicjalizacji konstruktor zgodnie z wymiarami tworzy tablicę dwuwymiarową obiektów przycisków/pól na planszy, dodatkowo tworzy zmienne charakteryzujące oba jej wymiary (długość i szerokość), liczbę min i inne sumaryczne informacje o przyciskach na planszy.
  - Program wyświetla nową **pustą planszę**. Robi to za pomocą **metody "wyswietl"**, która rysuje planszę pól o równych wymiarach. Przy tworzeniu każdego pola odwołuje się 
do **metody pola "pokaz"**, które wyświetla środek pola zgodnie z aktualnymi charakterystykami pola.
  - Co ważne bomby nie są jeszcze rozstawione na planszy. 
  - Następnie **użytkownik podaje numer dowolnie wybranego pola** - będzie to pole zawsze puste (wolne od miny), ponieważ **losowanie odbywa się dopiero po kliknięciu pierwszego pola**, przeprowadzając losowanie na wszystkich pozostałych.
  - Podczas rozstawiania min w metodzie planszy **(rozstaw_miny)** następuje jednocześnie **aktualizowanie liczników bomb** sąsiadujących dla każdego pola. **(zmienna pola "sasiednie_bomby")**
  - Przeprowadzaniem całej rozgrywki steruje **pętla while w funkcji głównej main**, którą przerywa dopiero sygnał o bombie lub wygranej.
  - **Użytkownik** przy każdym przejściu podaje **jeden z trzech trybów** (który odpowiada kliknięciu, oflagowaniu lub oznaczeniu pytajnikiem) danego pola i **współrzędne tego pola na którym chce działać**. Uzyskane z wejścia zmienne są przekazywane do metody planszy **pojedynczy_ruch**.
  - Tam następuje interakcja z danym polem poprzez **metodę "interakcja"**. Następnie plansza jest wyświetlana i sprawdzany jest warunek wygranej. **Wygrana następuje, gdy odkryte są wszystkie pola bez min, lub gdy oflagowane są wszystkie i tylko te, pola z minami.**
  - Następuje powielenie tych czynności aż do momentu, gdy użytkownik kliknie na bombę (czyli nastąpi kliknięcie "k" na pole, którego zmienna "bomba" zwraca True), lub 1 z warunków wygranej zostanie spełniony (zwróci True). **Na tym gra się kończy.**

- CHARAKTERYSTYCZNE ELEMENTY KODU:
  - W kodzie zastosowałem **szereg konstrukcji** takich jak:
    - List comprehensions
    - Klasy
    - Moduły

- PROBLEMY
  - Przy tworzeniu projektu największe trudności sprawiły mi testy, gdyż okazało się, że konieczne jest przekształcenie całości kodu i obudowanie go w funkcje, by móc poprawnie i wydajnie testować za pomocą modułu unittest i jego metod assertTrue, assertFalse i assertEqual. 
  - Niestety, w przypadku grafiki musiałem poprzestać na interfejsie konsoli, ze względu na ograniczenie czasowe.
