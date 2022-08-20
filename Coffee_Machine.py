from art import logo
import pandas as pd
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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def process_coins():
    '''Returns the total calculated from coins inserted.'''
    print("Please, insert coins")
    total=int(input("How many quarters do you want to insert? "))*0.25
    total+=int(input("How many dimes do you want to insert? " )) * 0.10
    total+=int(input("How many nickels do you want to insert? " )) * 0.05
    total+=int(input("How many pennies do you want to insert? " )) * 0.01
    return total
def is_transaction_succesfull(money_received, total_cost):
    if money_received>=total_cost:
        change=money_received-total_cost
        print(f"Thank you for your purchase! Your change is ${change}")
        global profit
        profit+=change
        return True
    else:
        print("Sorry, not enough money. Please try again.")
        return False

'''7. Make coffee. 
      a. If the transaction is succesfull and there are enough resources to make the drink the 
         user selected, then the ingredients to make the drink should be deducted from the 
         coffee machine resources.
'''
def make_coffee(drink_name, order_ingredients): #choice=drink_name, drink["ingredients"]
    for item in order_ingredients: 
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}☕")

def check_resources(resources, ingredients):
    for resource in ingredients:
        if resources[resource]<ingredients[resource]:
            print(f"Sorry therre is not enough {resource}. Please try to choose another coffee.")
            return False
    return True

'''1. Prompt user by asking "What would you like? (espresso, latte, cappuccino):
         a. Check the user's input to decide what to do next
         b. The prompt should show every tinme action has completed, e.g. once the drink is
            dispensed. The prompt should show again to serve the next customer.
'''
is_on=True

print(logo)
print("\nWelcome to the coffee machine!")
while is_on: #while loop to keep the program running
    print("\n$Prices$")
    print(f"\nLatte is in ${MENU['latte']['cost']}")
    print(f"Espresso is in ${MENU['espresso']['cost']}")
    print(f"Cappuccino is in ${MENU['cappuccino']['cost']}")
    choice=input("\nWhat would you like? (espresso, latte, cappuccino): ")
    '''2. Turn off the Coffe Machine by entering "off" to the prompt. 
            a. For maintainers of the coffee machine, they can use "off" as the secret word to turn off the machine.
            Your code should end execution when the user enters "off".'''
    
    if choice=="off":
        is_on=False #ends the loop
        '''3. Print report. 
            a. Whenn the user enters "report" to the prompt, a report should be generated that shows
            the current resource values. e.g.
            water: 100ml
            milk: 50ml
            coffee: 76g
            Money: $2.5'''
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

        '''4. Check resources sufficient?
              a. When the user chooses a drink, the program should check if there are enough
               resources to make that drink.
               b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
                  It should not continue to make the drink but print: "Sorry there is not enough water."
                c. The same should happen if another resource is depleted, e.g. milk or coffee'''
    else:
        drink=MENU[choice] #gets the drink from the menu
        print(drink["ingredients"])
        if check_resources(resources, drink["ingredients"]): #checks if the resources are sufficient
        
            '''5. Process coins. 
                  a. If there are sufficient resources, to make the drink selected, then the program should
                     prompt the user to inser coins.
                  b. Remember that quarters = $0.25, dimes= $0.1, nickels = $0.05, and pennies = $0.01.
                  c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 * 2 + 0.05 * 0.01 *2 = $0.52'''
            payment=process_coins()
            '''6. Check transaction successful? 
                  a. Check that the user has inserted enough money to purchase the drink they selected.
                     E.g. Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
                     program should say "Sorry that's not enough money. Money refunded."
                  b. But if the user has inserted enough money, then the cost of the drinkg gets added to the machine 
                     as the profit and this will be reflected in the next time "report" is triggered. E.g. 
                     Water: 100ml
                     Milk: 50ml
                     Coffee: 76g
                     Money: $2.52
                  c. If the user has inserted too much oney, the machine should offer change.
                     E.g. "Here is $2.45 dollars in change." The change should be rounded to 2 decimal places.'''
            if is_transaction_succesfull(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])

