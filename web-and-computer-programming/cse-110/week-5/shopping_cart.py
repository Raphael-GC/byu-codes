# Author: Raphael Carneiro
# Week 5 Project: Shopping Cart

import os

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
    item = input("Which item would you like to remove? ")

    # Removing by index
    if item.isdigit():
        index = int(item) - 1
        if 0 <= index < len(shopping_cart):
            shopping_cart.pop(index)
            print(f"Item {index} removed.")
            print("Test do remove por numero")
        else:
            # Error message
            print("Please enter a valid item number within the current list.")
    # Removing by name
    else:
        for i in range(len(shopping_cart)):
            if item.lower() == shopping_cart[i][0].lower():
                shopping_cart.pop(i)
            print(f"Item {i+1} removed.")
            print("Test do remove por nome")
            return
        # Error message
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

# Menu options
while True:
    print("\n🛒 Shopping Cart 🛒")
    print()
    print("What would you like to do?")
    print("1. ➕ Add item")
    print("2. 👀 View cart")
    print("3. ➖ Remove item")
    print("4. 🟰 Compute total")
    print("5. 🔚 Quit")
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
        print("\nThank you. Goodbye.👋🏾 ")
        break
    else:
        print("Please enter a valid choice.")
        continue
