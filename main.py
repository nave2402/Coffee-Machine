from Data import MENU,Storage


espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
espresso_cost = MENU["espresso"]["cost"]
latte_water = MENU["latte"]["ingredients"]["water"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_cost = MENU["latte"]["cost"]
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_cost = MENU["cappuccino"]["cost"]


def change(price, quarters, dimes, nickles, pennies):
    pennie = 0.01
    nickle = 0.05
    dime = 0.1
    quarter = 0.25
    pennies *= pennie
    nickles *= nickle
    dimes *= dime
    quarters *= quarter
    sum_pay = quarters + dimes + nickles + pennies
    change = sum_pay - price
    if sum_pay >= price:
        print(f"Your change is: {change} $")
        print(f"Here is your {choice} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
    return change


def check_storge(choice):
    if choice == "espresso":
        if MENU[choice]["ingredients"]["water"] > Storage["water"]:
            return "Sorry there is not enough water"
        elif MENU[choice]["ingredients"]["coffee"] > Storage["coffee"]:
            return "Sorry there is not enough coffee"
    elif choice == "latte" or choice == "cappuccino":
        if MENU[choice]["ingredients"]["water"] > Storage["water"]:
            return "Sorry there is not enough water"
        elif MENU[choice]["ingredients"]["coffee"] > Storage["coffee"]:
            return "Sorry there is not enough coffee"
        elif MENU[choice]["ingredients"]["milk"] > Storage["milk"]:
            return "Sorry there is not enough milk"


def coffee(choice):
    if check_storge(choice=choice):
        print(check_storge(choice=choice))
    else:
        if choice == "cappuccino":
            price = 3
        elif choice == "latte":
            price = 2.5
        elif choice == "espresso":
            price = 1.5
        print(f"The price of {choice} is: {price} $")
        print("How do you want to pay?")
        quarters = int(input("How many quarters (0.25)? "))
        dimes = int(input("How many dimes (0.1)? "))
        nickles = int(input("How many nickles (0.05)? "))
        pennies = int(input("How many pennies (0.01)? "))
        value = change(price=price, quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)
        return value



def format_report():
    water = Storage["water"]
    milk = Storage["milk"]
    coffee = Storage["coffee"]
    money = Storage["money"]
    return f"water: {water} ml\nmilk: {milk} ml\ncoffee: {coffee} g\nmoney: {money} $"


def report(choice):
    if choice == "espresso":
        Storage["water"] -= espresso_water
        Storage["coffee"] -= espresso_coffee
        Storage["money"] += espresso_cost
    elif choice == "latte":
        Storage["water"] -= latte_water
        Storage["milk"] -= latte_milk
        Storage["coffee"] -= latte_coffee
        Storage["money"] += latte_cost
    elif choice == "cappuccino":
        Storage["water"] -= cappuccino_water
        Storage["milk"] -= cappuccino_milk
        Storage["coffee"] -= cappuccino_coffee
        Storage["money"] += cappuccino_cost
    elif choice == "report":
        print(format_report())


should_continue = True
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report(choice=choice)
    elif choice == "off":
        should_continue = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if not check_storge(choice=choice) and coffee(choice=choice) > 0:
            report(choice=choice)
        elif check_storge(choice=choice):
            print(check_storge(choice=choice))




    # else:
    #     coffee(choice=choice)
    #     if not check_storge(choice=choice) and coffee(choice=choice) > 0:
    #         report(choice=choice)






