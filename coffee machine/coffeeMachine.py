import math

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
def get_total_coins(quarters,dimes,nickles,pennies):
    return (quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01)

def get_drink(type_drink,coins):
    global profit
    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]
    water_req = MENU[type_drink]['ingredients']['water']
    coffee_req = MENU[type_drink]['ingredients']['coffee']
    money_req = MENU[type_drink]['cost']
    if (water_req > water_available):
        return print(f"Sorry there is not enough water to make a {type_drink}")
    if (coffee_req > coffee_available):
        return print(f"Sorry there is not enough coffee to make a {type_drink}")
    if (type_drink != "espresso"):
        milk_req = MENU[type_drink]['ingredients']['milk']
        if milk_req > milk_available:
            return print(f"Sorry there is not enough milk to make a {type_drink}")
    if (coins < money_req):
        return print(f"Sorry that's not enough money. The price is {money_req}")
    resources['water'] -= water_req
    if (type_drink!='espresso'):
        resources["milk"] -=  milk_req
    resources["coffee"] -= coffee_req
    if (coins > money_req):
        change = math.ceil((coins - money_req)*100)/100
        profit += money_req
    else:
        change = 0
        profit += coins
    print(f"Here is your {type_drink} ☕")
    print(f"Your change comes out to be ${change}")
    return change
wants_drink = True
while wants_drink:
    drink_choice = input("What would you like? (espresso/latte/cappuccino/exit): ")
    if (drink_choice == "exit"):
        wants_drink = False
        print("Coffee machine is terminated")
    elif (drink_choice == "report"):
        print(f'water: {resources["water"]}ml')
        print(f'milk: {resources["milk"]}ml')
        print(f'coffee: {resources["coffee"]}g')
        print(f'money: ${profit}')
    else:
        if (drink_choice == "espresso" or drink_choice == "latte" or drink_choice == "cappuccino"):
            print("Please insert coins. ")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            total_coins = get_total_coins(quarters,dimes,nickles,pennies)
            get_drink(drink_choice,total_coins)
        else:
            print("Enter one of the available drink options: espresso,latte,cappuccino")



