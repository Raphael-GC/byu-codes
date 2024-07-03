# Overview: This activity dives deeper into working with lists.
# Instructions:
# Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."

import os
itens = []
purchase = 'inf'

print("Please enter the items of the shopping list (type: quit to finish): ")

while purchase != 'quit':
    purchase = input("Item: ")
    if purchase != 'quit':
        itens.append(purchase)

print("\nThe shopping list is:")
for item in itens:
    print(item.title())

print("\nThe shopping list with indexes is:")
for i,item in enumerate(itens):
    print(f"{i}. {item.title()}")

index_num = int(input("\nWhich item would you like to change? "))
new_purchase = input("What is the new item? ")
itens.pop(index_num)
itens.insert(index_num, new_purchase)

print("\nThe shopping list with indexes is:")
for i,item in enumerate(itens):
    print(f"{i}. {item.title()}")
    