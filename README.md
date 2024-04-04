Lab02 - zadani typu:
1. [2pkt] Rozszerzenie zadania 5 z poprzedniego zestawu - pola figur
Napisz prosty program do obliczania pola figur geometrycznych. Użytkownik wybiera pole figury spośród dostępnych w zdefiniowanej liście 3-elementowej (np. prostokąt, trapez, koło, trójkąt, deltoid) - wpisując odpowiedniego stringa.
Sprawdź, czy wpisana nazwa znajduje się w liście, jeśli nie, program kończy się. Następnie dla wybranej figury użytkownik podaje parametry do obliczenia pola w odpowiedniej ilości (bok, wysokość, średnica itp.), w ramach tylko jednej
instrukcji input(), oddzielone spacją. Następnie zapisz parametry dla każdej figury w jednej liście, wykorzystaj split(). Zweryfikuj, czy liczba parametrów jest poprawna i czy są to wartości dodatnie, jeśli nie, program kończy się. Następnie
oblicz i wyświetl pole danej figury, ale do obliczeń wykorzystując tylko elementy listy i odpowiednie operacje indeksowania, bez pomocniczych zmiennych do parametrów figury.
2. [2pkt] Zdefiniuj słownik, którego wartościami będą wydatki na życie w ostatnich kilku miesiącach, a kluczami nazwy miesięcy. Wyznacz i wyświetl wartość minimalną, maksymalną, sumę i wartość średnią (wykonaj odpowiednie operacje na
liście wartości). Sprawdź czy kwota za ostatni miesiąc (nie istnieje prosty sposób na “automatyczne” wybranie ostatniego miesiąca ze słownika, odwołaj się po prostu do nazwy) przekracza wartość średnią - jeśli tak, to wyświetl tekst
ostrzeżenia “zacznij oszczędzać”, a jeśli nie, informację “jesteś bezpieczny”.
3. [2pkt] Formularz rejestracji
Poproś użytkownika o wpisanie (inputy) imienia, nazwiska, daty urodzenia w narzuconym formacie dd-mm-rrr oraz maila. Przy pomocy operacji na elementach listy, napisz proste walidatory dla daty urodzenia i maila (ma spełniać tylko
prosty schemat “tekst@tekst”, zawierać co najmniej jedną kropkę i nie zaczynać się od cyfry, bez konieczności użycia wyrażeń regularnych, poszukaj odpowiednich funkcji dla stringów do sprawdzania czy znak jest literą, liczbą, itd).
Następnie przedstaw wpisane dane w postaci słownika, zawierającego zaszyfrowane dane w schemacie:
{imię i nazwisko: P**** M*** (złączone razem dane z dwóch inputów, połączone spacją, tylko pierwsze litery, zamienione na duże jeśli użytkownik wpisał małe, reszta w postaci gwiazdek);
wiek: 32 (obliczony na podstawie tylko roku urodzenia);
mail: p********@gmail.com (tylko pierwsza litera maila, reszta przed @ to gwiazdki, domena zostaje bez zmian)}
4. [4pkt] Odczyt danych i walidacja numeru PESEL
Użytkownik wpisuje numer PESEL w postaci stringa (zahardkodowana wartość na początku kodu lub input). Przedstaw go w postaci listy lub krotki (każda cyfra pod osobnym indeksem).
Uwaga: cyfry numeru PESEL po podzieleniu na znaki będą wciąż stringami, dlatego może się przydać operacja rzutowania wszystkich elementów na liczby - niestety wymaga to zastosowania pętli for lub list comprehension - wykorzystaj
jeden ze sposobów z Python | Converting all strings in list to integers - GeeksforGeeks . Można też tego uniknąć i rzutować za każdym razem elementy do typu int przy obliczeniach (mało wygodne i zgrabne, ale możliwe) . Wykorzystując
wiadomości z PESEL – Wikipedia, wolna encyklopedia oraz operacje na elementach listy, zwaliduj poprawność wpisanego numeru PESEL (długość, dzień, miesiąc i rok, cyfra kontrolna - tu stwórz pomocniczą listę z wagami; ogranicz się
tylko do urodzonych w stuleciach 1900+ i 2000+) - w przypadku braku spełnienia któregoś kryterium wyświetl stosowną informację; a jeśli PESEL jest poprawny, odczytaj z niego i przedstaw w formie słownej: datę urodzenia* oraz płeć (* -
miesiąc może być podany liczbowo, ale możesz też wyszukać w sieci prosty sposób na pozyskanie nazwy miesiąca w Pythonie). Do testowania skorzystaj z generatora online, np. http://generatory.it/ lub (dla zaawansowanych) zapoznaj się z
możliwościami biblioteki Faker ( Locale pl_PL — Faker 24.0.0 documentation )

Lab3 - zadania typu:
1. Napisz program wyświetlający w każdej linijce następujące liczby:
a) 0,3,6,9,12 (z użyciem for - max 3 linijki)
b) 3,2,1,0,-1,-2,-3 (z użyciem while - max 4 linijki)
2. Korzystając tylko z instrukcji, które omawialiśmy już na zajęciach napisz program, który wyświetla trójkąt Pascala dla dowolnego poziomu x podanego przez użytkownika.
Konstrukcja trójkąta Pascala i algorytm można znaleźć np. tutaj: https://pl.wikipedia.org/wiki/Tr%C3%B3jk%C4%85t_Pascala (uwaga! kod w Pythonie podany na stronie korzysta z
funkcji i list comprehensions - ich znajomość nie jest jednak konieczna do wykonania zadania). Do poprawnego wyświetlania przydatna będzie jedna nowa instrukcja center(),
która pozwala na wyświetlenie stringa w postaci “wyśrodkowanej” (poszukaj w sieci, jak zastosować tą instrukcję dla dowolnego stringa - w tym przypadku do każdego poziomu
trójkąta).
3. W innych językach programowania można spotkać pętlę do-while, nie ma jej natomiast bezpośrednio w Pythonie. Różni się ona od klasycznego while tym, że warunek logiczny dla
while sprawdzany jest na końcu instrukcji, a nie na początku (czyli instrukcje w pętli zawsze wykonają się co najmniej jeden raz). Zaprojektuj podobną konstrukcję logiczną,
korzystając z poznanych pętli i instrukcji. Instrukcje wewnątrz pętli są dowolne, ale takie aby pętla kiedyś mogła się przerwać.
4. Z wykorzystaniem rekurencji napisz funkcję, która:
a. poda n-ty wyraz ciągu Fibonacciego - algorytm: https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
b. obliczy wartość symbolu Newtona (funkcja dwóch zmiennych n i k) - algorytm: https://en.wikipedia.org/wiki/Binomial_coefficient
Uwaga! Oba podpunkty zadania da się wykonać na wiele różnych sposobów, ale zależy nam na wykorzystaniu rekurencji.
5. Napisz funkcję, która jako argument przyjmuje imię, a następnie zwraca wynik “kobieta” lub “mężczyzna”. Skorzystaj z pewnej własności standardowych polskich imion, która w
zdecydowanej większości się tutaj sprawdzi, zignoruj wyjątki. Następnie zdefiniuj tablicę z 5 różnymi imionami znajomych i wykorzystując stworzoną funkcję stwórz słownik, który
zawiera pary imię : płeć, a następnie przy pomocy lambdy posortuj słownik wartościami - najpierw kobiety, potem mężczyźni.

