Testy automatyczne dla systemu/aplikacji ekspresu do kawy
1. Struktura systemu/aplikacji
System/aplikacja ekspresu do kawy składa się z następujących komponentów:

Klasa CoffeeMachine: Reprezentuje ekspres do kawy. Ma możliwość ustawienia stanu i wykonania operacji parzenia kawy.
Klasy stanów kawy: WhiteCoffeeState, BlackCoffeeState, LatteState, AmericanoState, EspressoState, DoubleEspressoState. Każdy stan implementuje metodę brew_coffee(), która symuluje parzenie kawy.
2. Scenariusze testów
a. Testy jednostkowe:
Test metody brew_coffee() w klasie WhiteCoffeeState:

Sprawdza, czy metoda brew_coffee() wykonuje metodę _brew_coffee().
Test metody set_state() w klasie CoffeeMachine:

Sprawdza, czy po ustawieniu stanu w ekspresie do kawy, atrybut _state jest poprawnie ustawiony.
Test metody brew_coffee() w klasie CoffeeMachine z ustawionym stanem:

Sprawdza, czy po wykonaniu metody brew_coffee() w ekspresie do kawy z ustawionym stanem, nie zostaje zwrócony żaden wynik.
b. Testy integracyjne:
Test integracji ekspresu do kawy z różnymi stanami:
Sprawdza, czy po ustawieniu różnych stanów w ekspresie do kawy i wykonaniu metody brew_coffee(), nie zostaje zwrócony żaden wynik.
c. Test akceptacyjny:
Scenariusz testowy: Parzenie espresso:
Krok 1: Użytkownik posiada ekspres do kawy.
Krok 2: Użytkownik wybiera opcję "Espresso".
Krok 3: Oczekiwane jest, że ekspres do kawy zaparzy espresso.
3. Wykorzystane narzędzia i biblioteki
pytest: Biblioteka do uruchamiania testów jednostkowych, integracyjnych i akceptacyjnych w języku Python.
pytest-bdd: Rozszerzenie dla pytest, umożliwiające pisanie testów w stylu BDD (Behavior-Driven Development).
4. Ewentualne problemy i ich rozwiązania
Problem: Brak modułu pytest lub pytest-bdd.
Rozwiązanie: Upewnij się, że masz zainstalowane biblioteki pytest i pytest-bdd. Możesz zainstalować je za pomocą narzędzia pip: pip install pytest pytest-bdd.
Problem: Testy nie przechodzą lub nie działają zgodnie z oczekiwaniami.
Rozwiązanie: Sprawdź, czy implementacja kodu aplikacji jest zgodna z testami. Upewnij się, że metody są poprawnie zaimplementowane i zwracają oczekiwane wyniki lub wykonują oczekiwane akcje. Sprawdź również, czy testy pokrywają różne przypadki i scenariusze.
