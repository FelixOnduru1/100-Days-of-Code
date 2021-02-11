from requirements import MENU
from requirements import resources


def ingredients_checker(drink):
    ingredients = MENU[drink]["ingredients"]
    return ingredients


def cost_checker(drink):
    cost = MENU[drink]["cost"]
    return cost


def sufficiency_checker(drink):
    available_water = resources["water"]
    available_milk = resources["milk"]
    available_coffee = resources["coffee"]
    if drink == "espresso":
        if MENU[drink]["ingredients"]["water"] > available_water:
            print("Sorry, there is no enough water.")
        elif MENU[drink]["ingredients"]["coffee"] > available_coffee:
            print("Sorry, there is not enough coffee.")
        else:
            return "sufficient"
    else:
        if MENU[drink]["ingredients"]["water"] > available_water:
            print("Sorry, there is no enough water.")
        elif MENU[drink]["ingredients"]["milk"] > available_milk:
            print("Sorry, there is not enough milk.")
        elif MENU[drink]["ingredients"]["coffee"] > available_coffee:
            print("Sorry, there is not enough coffee.")
        else:
            return "sufficient"


def resource_deduct(drink):
    if drink == "espresso":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


money = 0
coffee_machine_active = True
print("Welcome to the Coffee Machine.")
while coffee_machine_active:
    customer_want = input("What would you like?\n").lower()

    if customer_want == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${money}")

    elif sufficiency_checker(drink=customer_want) == "sufficient":
        print("Please insert coins.")
        quarters = int(input("How many quarters?\n"))
        dimes = int(input("How many dimes?\n"))
        nickels = int(input("How many nickels?\n"))
        pennies = int(input("How many pennies?\n"))
        customer_money = round(float((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (quarters * 0.25)), 2)

        if customer_money >= cost_checker(drink=customer_want):
            drink_cost = cost_checker(drink=customer_want)
            customer_balance = customer_money - drink_cost
            money += drink_cost
            resource_deduct(drink=customer_want)
            if customer_balance == 0:
                print(f"Here is your {customer_want} ☕. Enjoy!")
            else:
                print(f"Here is ${customer_balance} in change.")
                print(f"Here is your {customer_want} ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
