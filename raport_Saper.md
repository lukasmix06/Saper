**SPRAWOZDANIE Z PROJEKTU - SAPER**

- Jest to wersja z podstawową grafiką utworzoną w wierszu poleceń w konsoli. 

- GŁÓWNE KLASY:
  - Główny rdzeń programu stanowi **klasa "Plansza"**, która zawiera wiele metod, na niej odbywa się większość operacji i przekształceń. Zawiera ona w sobie **obiekty klasy - "Przycisk"**, która reprezentuje pojedyncze pole na planszy. 
  https://github.com/lukasmix06/Saper/blob/ebff595e40162d94eea17c0fafdbedf89d4d5498/main.py#L67-L76
  - Każde takie pole zawiera szereg zmiennych opisujących jego stan m.in czy zawiera bombę **(bomba)**, czy jest oflagowane **("flaga")**, czy chociażby czy pole jest już widoczne dla użytkownika, tzn. czy zostało już przez niego kliknięte **("widoczny")**.
  https://github.com/lukasmix06/Saper/blob/ebff595e40162d94eea17c0fafdbedf89d4d5498/main.py#L42-L49
  
- OMÓWIENIE FUNKCJONALNOŚCI:
  - Na początku programu **użytkownik jest proszony o podanie obu wymiarów planszy**, aż do momentu gdy będą one spełniały odpowiednie kryteria wielkości. **(funkcja dobre_wymiary)**
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L22-L39
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L8-L12
  - Następnie **użytkownik podaje liczbę min**, która musi być mniejsza od liczby pól. **(funkcja dobre_miny)**.
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L15-L19
  - Gdy program pobierze od użytownika potrzebne i prawidłowe dane przekazuje je do **nowotworzonego obietku planszy**. Podczas inicjalizacji konstruktor zgodnie z wymiarami tworzy tablicę dwuwymiarową obiektów przycisków/pól na planszy, dodatkowo tworzy zmienne charakteryzujące oba jej wymiary (długość i szerokość), liczbę min i inne sumaryczne informacje o przyciskach na planszy.
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L192
  - Program wyświetla nową **pustą planszę**. Robi to za pomocą **metody "wyswietl"**, która rysuje planszę pól o równych wymiarach. Przy tworzeniu każdego pola odwołuje się 
do **metody pola "pokaz"**, które wyświetla środek pola zgodnie z aktualnymi charakterystykami pola.
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L104-L115
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L51-L64
  - Co ważne bomby nie są jeszcze rozstawione na planszy. 
  - Następnie **użytkownik podaje numer dowolnie wybranego pola** - będzie to pole zawsze puste (wolne od miny), ponieważ **losowanie odbywa się dopiero po kliknięciu pierwszego pola**, przeprowadzając losowanie na wszystkich pozostałych.
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L85-L102
  - Podczas rozstawiania min w metodzie planszy **(rozstaw_miny)** następuje jednocześnie **aktualizowanie liczników bomb** sąsiadujących dla każdego pola. **(zmienna pola "sasiednie_bomby")**
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L96-L102
  - Przeprowadzaniem całej rozgrywki steruje **pętla while w funkcji głównej main**, którą przerywa dopiero sygnał o bombie lub wygranej.
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L206-L213
  - **Użytkownik** przy każdym przejściu podaje **jeden z trzech trybów** (który odpowiada kliknięciu, oflagowaniu lub oznaczeniu pytajnikiem) danego pola i **współrzędne tego pola na którym chce działać**. Uzyskane z wejścia zmienne są przekazywane do metody planszy **pojedynczy_ruch**.
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L207
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L158-L182
  - Tam następuje interakcja z danym polem poprzez **metodę "interakcja"**. Następnie plansza jest wyświetlana i sprawdzany jest warunek wygranej. 
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L127-L156
  - **Wygrana następuje, gdy odkryte są wszystkie pola bez min, lub gdy oflagowane są wszystkie i tylko te, pola z minami.**
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L170-L182
  - Następuje powielenie tych czynności aż do momentu, gdy użytkownik kliknie na bombę (czyli nastąpi kliknięcie "k" na pole, którego zmienna "bomba" zwraca True), lub 1 z warunków wygranej zostanie spełniony (zwróci True). **Na tym gra się kończy.**
  https://github.com/lukasmix06/Saper/blob/98a4a14aa82e7def3765860a77dce20d1bdbdaad/main.py#L210-L211

- CHARAKTERYSTYCZNE ELEMENTY KODU:
  - W kodzie zastosowałem **szereg konstrukcji** takich jak:
    - List comprehensions
    https://github.com/lukasmix06/Saper/blob/ebff595e40162d94eea17c0fafdbedf89d4d5498/main.py#L70
    https://github.com/lukasmix06/Saper/blob/ebff595e40162d94eea17c0fafdbedf89d4d5498/main.py#L92-L93
    https://github.com/lukasmix06/Saper/blob/ebff595e40162d94eea17c0fafdbedf89d4d5498/main_test.py#L47
    - Klasy
    - Moduły

- PROBLEMY
  - Przy tworzeniu projektu największe trudności sprawiły mi testy, gdyż okazało się, że konieczne jest przekształcenie całości kodu i obudowanie go w funkcje, by móc poprawnie i wydajnie testować za pomocą modułu unittest i jego metod assertTrue, assertFalse i assertEqual. 
  - Niestety, w przypadku grafiki musiałem poprzestać na interfejsie konsoli, ze względu na ograniczenie czasowe.
