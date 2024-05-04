# Author: Raphael Carneiro
# Week 02 - Project Final Requirements

# Getting the meals prices
price_childs_meal = float(input("What is the price of a child's meal? ")) 
price_adults_meal = float(input("What is the price of an adult's meal? "))

# Getting the drinks prices. (This is a plus information)
price_childs_drink = float(input("What is the price of a child's drink? ")) 
price_adults_drink = float(input("What is the price of an adult's drink? "))

# Getting the people quantity
qty_children = int(input("How many children are there? "))
qty_adults = int(input("How many adults are there? "))

# Getting the desert price and quantity (This is a plus information)
price_dessert = float(input("What is the price of a dessert? "))
qty_dessert = int(input("How many desserts would you like? "))

# Calculating and displaying the Subtotal
subtotal = ((price_childs_meal + price_childs_drink) * qty_children) + ((price_adults_meal + price_adults_drink) * qty_adults) + (price_dessert * qty_dessert)
print(f"\nSubtotal: ${subtotal:.2f}")

# Getting the Sales Tax Rate and Calculating and displaying the Sales Tax
sales_tax_rate = float(input("\nWhat is the sales tax rate (%) ? "))
sales_tax = (subtotal * sales_tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")

# Getting the tip amount (This is a plus information)
tip_amount = float(input("What is the tip amount? "))

# Calculating and displaying the Total Amount
total_amount = subtotal + sales_tax + tip_amount
print(f"Total: ${total_amount:.2f}")

# Getting the payment amount, calculating the change amount and displaying it. 
payment_amount = float(input("\nWhat is the payment amount? "))
change_amount = payment_amount - total_amount
print(f"Change: ${change_amount:.2f}")