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

def check_resource(order):
    enough = True
    for resource in MENU[order]["ingredients"]:
        if(resources[resource] < MENU[order]["ingredients"][resource]):
            enough = False
    return enough


def print_report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Money: {money}")

money=0
machine_on = True

while(machine_on):
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order=="report":
        print_report()
    elif order=="off":
        print("Machine is turned off.")
        machine_on = False
    else:
        if check_resource(order):
            print("Please insert coins")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many quarters?: "))
            nickle = int(input("How many quarters?: "))
            pennies = int(input("How many quarters?: "))
            user_money = round(quarter*0.25 + dime*0.10 + nickle*0.05 + pennies*0.01, 2)
            print(f"User money: {user_money}")

            if(user_money>=MENU[order]["cost"]):
                change = user_money - MENU[order]["cost"]
                print(f"Here is {change} in change.")
                for resource in MENU[order]["ingredients"]:
                    resources[resource] -= MENU[order]["ingredients"][resource]
                money+=MENU[order]["cost"]
                print(f"Here is your {order}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry we have Insufficient resources to make {order}. Money refunded.")