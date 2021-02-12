from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    options = menu.get_items()
    choice = input(f"What would you like ({options}):\n").lower()
    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name=choice)
        if coffee_maker.is_resource_sufficient(drink=drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(order=drink)
