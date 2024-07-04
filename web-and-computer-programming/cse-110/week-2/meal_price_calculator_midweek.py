# Author: Raphael Carneiro
# Week 02 - Project Midweek Requirements

price_childs_meal = float(input("What is the price of a child's meal? ")) 
price_adults_meal = float(input("What is the price of an adult's meal? "))
qty_children = int(input("How many children are there? "))
qty_adults = int(input("How many adults are there? "))

subtotal = (price_childs_meal * qty_children) + (price_adults_meal * qty_adults)
print(f"\nSubtotal: ${subtotal}")
