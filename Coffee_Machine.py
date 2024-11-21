MENU = {
    "1": "espresso",
    "2": "latte",
    "3": "cappuccino"
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200
}

total_coffee_price_dict = {
    "espresso": 0.50,
    "latte": 1.50,
    "cappuccino": 2.50
}

def coffee_machine():
    while True:
        user_choice: str = input("What would you like? You can have an espresso (1), latte (2), or cappuccino (3): ").strip()
        if user_choice in MENU:  # Only proceed if the user choice is valid
            coffee_name = MENU[user_choice]
            price = total_coffee_price_dict[coffee_name]  
            print(f"The price of {coffee_name} is ${price:.2f}")  
            if check_resources(coffee_name):
                payment = process_coins()
                make_coffee(coffee_name, payment, price)
                break  
            else:
                print("Sorry, not enough resources to make this coffee.")
                break  
        else:
            print("Invalid choice. Rerun the program.")
            break  

def check_resources(coffee_name: str) -> bool:
    if coffee_name == "espresso":
        return resources["water"] >= 50 and resources["coffee"] >= 18
    elif coffee_name == "latte":
        return resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24
    elif coffee_name == "cappuccino":
        return resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 28
    return False

def process_coins() -> float:
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

def make_coffee(coffee_name: str, payment: float, price: float):
    prices = total_coffee_price_dict  

    if payment < prices[coffee_name]:
        print("Insufficient payment. Transaction canceled.")
    else:
        print(f"Making your {coffee_name}. Machine turned off.")
        if coffee_name == "espresso":
            resources["water"] -= 50
            resources["coffee"] -= 18
        elif coffee_name == "latte":
            resources["water"] -= 200
            resources["milk"] -= 150
            resources["coffee"] -= 24
        elif coffee_name == "cappuccino":
            resources["water"] -= 250
            resources["milk"] -= 100
            resources["coffee"] -= 28
        change = payment - prices[coffee_name]
        if change > 0:
            print(f"Here's your change: ${change:.2f}")

if __name__ == "__main__":
    coffee_machine()
