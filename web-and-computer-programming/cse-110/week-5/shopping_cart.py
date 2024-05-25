# Author: Raphael Carneiro
# Week 5 Project: Shopping Cart

import os
# Cleaning up the terminal screen before showing the program.
os.system('cls')

# Create a shopping cart list
shopping_cart = []

# Introduction
print("Welcome to the Shopping Cart Program!")

# Create a add-item function
def add_item():
    os.system('cls')
    print("🛒 Shopping Cart 🛒")
    print()
    item = input("What item would you like to add? ")
    price = float(input("What is the price of the item? "))
    shopping_cart.append((item, price))
    print(f"'{item.lower()}' has been added to the cart.")

# Create a view_cart function
def view_cart():
    os.system('cls')
    print("The contents of the shopping cart are: 🛒")
    for i in range(len(shopping_cart)):
        item, price = shopping_cart[i]
        print(f"{i + 1}. {item.lower()} - ${price}")
    print("--------------------------------------------------------")

# Create a remove-item function
def remove_item():
    os.system('cls')
    print("🛒 Shopping Cart 🛒")
    print()
    item_remove = input("Which item would you like to remove? ")

    # Removing by index (number)
    if item_remove.isdigit():
        index = int(item_remove) - 1
        if 0 <= index < len(shopping_cart):
            shopping_cart.pop(index)
            print(f"Item {index + 1} removed.")

    # Removing by name (string) - (It's not a requirement)
    elif item_remove.isalpha():
        for i in range(len(shopping_cart)):
            if item_remove.lower() == shopping_cart[i][0].lower():
                shopping_cart.pop(i)
                print("Item removed.")

    # Error message
    else:
        print("Please enter a valid item name within the current list.")

# Create a compute_total function
def compute_total():
    os.system('cls')
    print("🛒 Shopping Cart 🛒")
    print()
    total = 0.0
    for i in range(len(shopping_cart)):
        price = shopping_cart[i][1]
        total += price
    print(f"The total price of the items in the shopping cart is: ${total:.2f} 💸")
    print("--------------------------------------------------------")
    return total

# Getting the payment amount, calculating the change amount and displaying it. (It's not a requirement)
def payment():
    if compute_total() != 0:
        payment_amount = float(input("\nWhat is the payment amount? "))
        change_amount = payment_amount - compute_total()
        print(f"Change: ${change_amount:.2f}")
    else:
        print("There are no items in the shopping cart.")

# Menu options
while True:
    print("\n🛒 Shopping Cart 🛒")
    print()
    print("What would you like to do?")
    print("1. ➕ Add item")
    print("2. 👀 View cart")
    print("3. ➖ Remove item")
    print("4. 🟰  Compute total")
    print("5. 💸 Payment") # (It's not a requirement)
    print("6. 🔚 Quit")
    try:
        choice = int(input("Please enter an action: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue
    if choice == 1:
        add_item()
    elif choice == 2:
        view_cart()
    elif choice == 3:
        remove_item()
    elif choice == 4:
        compute_total()
    elif choice == 5:
        payment()
    elif choice == 6:
        print("\nThank you. Goodbye.👋🏾 ")
        break
    else:
        print("Please enter a valid choice.")
        continue
