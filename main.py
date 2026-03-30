MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# TODO: 3. Format the resource-ingredient data into a printable format.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
inventory = {}

# TODO: 2. Create dictionaries for Currency Values.
currency = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

ESPRESSO_COST = MENU["espresso"]["cost"]
LATTE_COST = MENU["latte"]["cost"]
CAPPUCCINO = MENU["cappuccino"]["cost"]

COST = {
    "espresso": ESPRESSO_COST,
    "latte": LATTE_COST,
    "cappuccino": CAPPUCCINO,
}

espresso = COST["espresso"]
latte = COST["latte"]
cappuccino = COST["cappuccino"]

coffee_machine_on = True


def deduct(choice_i, penny, nickel, dime, quarter):
    cost = COST[choice_i]

    deducted_amount = add_amount(penny_i=penny, nickel_i=nickel, dime_i=dime, quarter_i=quarter) - cost

    return deducted_amount

def get_coins():
    return {
        "quarter": float(input("how many quarters?: ")),
        "dime" : float(input("how many dimes?: ")),
        "nickel": float(input("how many nickles?: ")),
        "penny": float(input("how many pennies?: ")),
    }


def add_amount(penny_i, nickel_i, dime_i, quarter_i):
    total_amount = (currency["penny"] * penny_i) + (currency["nickel"] * nickel_i) + (currency["dime"] * dime_i) + (
                currency["quarter"] * quarter_i)
    return total_amount


money = 0

while coffee_machine_on:
    # TODO: 1. Input Statements asking the user What they would like (Espresso/Latte/Cappuccino; add 'off' and 'report' as prompt)
    choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    # TODO: 4. Print "Please insert a coin."

    # TODO: 5. Inputs(how many quarters?:) (how many dimes?:) (how many nickels?:) (how many pennies?:)


    # TODO: 6. Sum up the inserted coins and calculate if it is enough to buy the drink ordered

    # TODO: 7. Check if the sum of coins inserted is enough to purchase the drink/flavor selected; and if not give feedback(insufficient amount)
    # TODO: 8. If coins inserted is enough to purchase the item, then deduct the sum from the total coins inserted and give change feedback.



    # TODO: 9. Deduct from resources if inserted coins is enough for purchase to be completed

    if choice == "espresso":
        print("Please insert coins.")
        coins = get_coins()
        change = deduct(choice, coins["penny"], coins["nickel"], coins["dime"], coins["quarter"])
        if change >= 0:

            if resources["water"] < MENU[choice]["ingredients"]["water"] or resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
                print(f"Sorry, Insufficient Ingredients!")
            else:
                money += COST[choice]
                print(f"Here is ${change:.2f} in change.")
                resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - 0
                resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
                print(f"Here is your {choice}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
            # coffee_machine_on = False
    elif choice == "latte":
        print("Please insert coins.")
        coins = get_coins()
        change = deduct(choice, coins["penny"], coins["nickel"], coins["dime"], coins["quarter"])
        if change >= 0:

            if resources["water"] < MENU[choice]["ingredients"]["water"] or resources["coffee"] < MENU[choice]["ingredients"]["coffee"] or resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
                print(f"Sorry, Insufficient Ingredients!")
            else:
                money += COST[choice]
                print(f"Here is ${change:.2f} in change.")
                resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
                print(f"Here is your {choice}. Enjoy!")
        else:
            print("Sorry that's not enough money and you are broke. Money refunded.")
            # coffee_machine_on = False
    elif choice == "cappuccino":
        print("Please insert coins.")
        coins = get_coins()
        change = deduct(choice, coins["penny"], coins["nickel"], coins["dime"], coins["quarter"])
        if change >= 0:

            if resources["water"] < MENU[choice]["ingredients"]["water"] or resources["coffee"] < \
                    MENU[choice]["ingredients"]["coffee"] or resources["coffee"] < MENU[choice]["ingredients"][
                "coffee"]:
                print(f"Sorry, Insufficient Ingredients!")
            else:
                money += COST[choice]
                print(f"Here is ${change:.2f} in change.")
                resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
                print(f"Here is your {choice}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
        print(f"Here is your bloody {choice}.")
    elif choice == "off":
        coffee_machine_on = False
    else:
        print("Try some of this inputs as options! 'espresso' or 'latte' or 'report' or 'cappuccino'")

    # TODO: 10. Print remaining resource-ingredient

    # TODO: 11. Print Here is your drink
    # TODO: 12. Repeat the process
