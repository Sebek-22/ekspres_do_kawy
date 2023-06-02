from abc import ABC, abstractmethod
import time




class CoffeeState(ABC):
    @abstractmethod
    def brew_coffee(self):
        pass


class WhiteCoffeeState(CoffeeState):
    def brew_coffee(self):
        print("Robię kawę białą... Czekaj!")
        self._brew_coffee()

    @staticmethod
    def _brew_coffee():
        time.sleep(30)
        print("Gotowe!")


class BlackCoffeeState(CoffeeState):
    def brew_coffee(self):
        print("Robię kawę czarną... Czekaj!")
        self._brew_coffee()

    @staticmethod
    def _brew_coffee():
        time.sleep(30)
        print("Gotowe!")


class LatteState(CoffeeState):
    def brew_coffee(self):
        print("Robię latte... Czekaj!")
        self._brew_coffee()

    @staticmethod
    def _brew_coffee():
        time.sleep(30)
        print("Gotowe")


class AmericanoState(CoffeeState):
    def brew_coffee(self):
        print("Robię Americano... Czekaj!")
        self._brew_coffee()

    @staticmethod
    def _brew_coffee():
        time.sleep(30)
        print("Gotowe!")


class EspressoState(CoffeeState):
    def brew_coffee(self):
        print("Robię Espresso... Czekaj!")
        self._brew_coffee()

    @staticmethod
    def _brew_coffee():
        time.sleep(30)
        print("Gotowe")


class DoubleEspressoState(CoffeeState):
    def brew_coffee(self):
        print("Robię DoubleEspresso... Czekaj!")
        self._brew_coffee()

    @staticmethod
    def _brew_coffee():
        time.sleep(30)
        print("Gotowe!")


class CoffeeMachine:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def brew_coffee(self):
        if self._state:
            self._state.brew_coffee()
        else:
            print("Nie wybrano żadnej opcji.")



def get_user_choice():
    print("Wybierz rodzaj kawy:")
    print("1. Kawa biała")
    print("2. Kawa czarna")
    print("3. Latte")
    print("4. Americano")
    print("5. Espresso")
    print("6. Podwójne Espresso")
    wybor = input("Podaj numer opcji: ")
    return wybor


machine = CoffeeMachine()

choice = get_user_choice()

if choice == "1":
    machine.set_state(WhiteCoffeeState())
elif choice == "2":
    machine.set_state(BlackCoffeeState())
elif choice == "3":
    machine.set_state(LatteState())
elif choice == "4":
    machine.set_state(AmericanoState())
elif choice == "5":
    machine.set_state(EspressoState())
elif choice == "6":
    machine.set_state(DoubleEspressoState())
else:
    print("Nieprawidłowy wybór.")

machine.brew_coffee()
