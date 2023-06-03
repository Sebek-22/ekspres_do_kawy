import pytest
from pytest_bdd import given, when, then
from ekspres_do_kawy import (
    CoffeeMachine,
    WhiteCoffeeState,
    BlackCoffeeState,
    LatteState,
    AmericanoState,
    EspressoState,
    DoubleEspressoState,
)

# Testy jednostkowe

def test_white_coffee_state_brew_coffee():
    state = WhiteCoffeeState()
    state.brew_coffee()  # Oczekujemy, że nie zostanie zgłoszony żaden błąd

def test_coffee_machine_set_state():
    machine = CoffeeMachine()
    state = WhiteCoffeeState()
    machine.set_state(state)

    assert machine._state == state

def test_coffee_machine_brew_coffee_with_state():
    machine = CoffeeMachine()
    state = WhiteCoffeeState()
    machine.set_state(state)

    result = machine.brew_coffee()

    assert result is None




# Testy integracyjne

def test_coffee_machine_integration_with_states():
    machine = CoffeeMachine()

    states = [
        WhiteCoffeeState(),
        BlackCoffeeState(),
        LatteState(),
        AmericanoState(),
        EspressoState(),
        DoubleEspressoState(),
    ]

    for state in states:
        machine.set_state(state)
        result = machine.brew_coffee()
        assert result is None  # Oczekujemy, że metoda brew_coffee() nie zwróci żadnego wyniku

# Test akceptacyjny

@pytest.mark.bdd
def test_coffee_machine_acceptance_scenario():
    machine = CoffeeMachine()

    @given("I have a coffee machine")
    def step_given_coffee_machine():
        pass

    @when("I select 'Espresso' option")
    def step_when_select_espresso():
        machine.set_state(EspressoState())

    @then("The coffee machine should brew an Espresso")
    def step_then_brew_espresso():
        result = machine.brew_coffee()
        assert result is None  # Oczekujemy, że metoda brew_coffee() nie zwróci żadnego wyniku

    # Uruchomienie testu
    step_given_coffee_machine()
    step_when_select_espresso()
    step_then_brew_espresso()
