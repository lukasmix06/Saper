PROJEKT GRY KOMPUTEROWEJ SAPER

Jest to wersja z podstawową grafiką utworzoną z wiersza poleceń w konsoli. 
Główny rdzeń programu stanowi klasa "Plansza", która zawiera wiele metod, na niej odbywa się większość operacji i przekształceń. Zawiera ona w sobie 
inną klasę - "Przycisk", która reprezentuje pojedyncze pole na planszy. Każde takie pole zawiera szereg zmiennych opisujących jej stan m.in czy zawiera bombę (bomba), 
jest oflagowana ("flaga"), czy chociażby czy pole jest już widoczne dla użytkownika, tzn. czy zostało już przez niego kliknięte ("widoczny").
Plansza przy inicjalizacji w konstruktorze, tworzy zmienne charakteryzujące oba jej wymiary (dlugość i szerokość), liczbę min i inne sumaryczne informacje o przyciskach 
na planszy.
Na początku programu użytkownik jest proszony o podanie obu wymiarów planszy, aż do momentu gdy będą one spełniały odpowiednie kryteria wielkości. (funkcja dobre_wymiary)
Następnie użytkownik podaje liczbę min, która musi być mniejsza od liczby pól. (dobre_miny).
Gdy program pobierze od użytownika potrzebne i prawidłowe dane przekazuje je do nowotworzonego obietku planszy, a konstruktor zgodnie z wymiarami tworzy tablicę dwuwymiarową obiektów przycisków/pól na planszy.
Program wyświetla nową pustą planszę. Robi to za pomocą metody "wyswietl", która tworzy planszę pól o równych wymiarach i przy tworzeniu każdego pola odwołuje się 
do metody pola "pokaz", które wyświetla środek pola zgodnie z aktualnymi danymi.
Co ważne bomby nie są jeszcze rozstawione na planszy. 
Następnie użytkownik podaje numer dowolnie wybranego pola - będzie to pole zawsze puste (wolne od miny), ponieważ losowanie odbywa się dopiero po kliknięciu pierwszego pola, przeprowadzając losowanie na wszystkich pozostałych.
Podczas rozstawiania min w metodzie planszy (rozstaw_miny) następuje jednocześnie aktualizowanie liczników bomb sąsiadujących dla każdego pola. (zmienna pola "sasiednie_bomby")
Przeprowadzaniem całej rozgrywki steruje pętla while w funkcji głównej main, którą przerywa dopiero sygnał o bombie lub wygranej.
Użytkownik przy każdym przejściu podaje jeden z trzech trybów (który odpowiada kliknięciu, oflagowaniu itp.) danego pola i współrzędne tego pola na którym chce działać. Uzyskane z wejścia zmienne są przekazywane do metody planszy pojedynczy_ruch.
Tam następuje interakcja z danym polem poprzez metodę "interakcja". Następnie plansza jest wyświetlana i sprawdzany jest warunek wygranej, wygrana następuje, gdy odkryte są wszystkie pola bez min, lub gdy oflagowane są wszystkie i tylko te, pola z minami.
Przy każdym przejściu planszy następuje pobranie danych od użytkownika i zastosowanie ich na planszy. Gra kończy się w momencie, gdy użytkownik kliknie na bombę (czyli nastąpi kliknięcie "k" na pole, którego zmienna "bomba" zwraca True), lub przy przejściu pętli 1 z warunków wygranej zostanie spełniony.

W kodzie zastosowałem szereg konstrukcji takich jak:
- List comprehensions
- Klasy
- Moduły

Przy tworzeniu projektu największe trudności sprawiły mi testy, gdyż okazało się, że konieczne jest przekształcenie całości kodu i obudowanie go w funkcje, by móc poprawnie i wydajnie testować za pomocą modułu unittest i jego metod assertTrue, assertFalse i assertEqual.
