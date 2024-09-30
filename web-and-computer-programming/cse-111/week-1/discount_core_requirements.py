# Author: Raphael Carneiro
# Week 01 - Individual Activity: Discounts

# Purpose:Improve your understanding of calling built-in Python functions
# and calling functions and methods that are in a standard Python module.

# Problem Statements: You work for a retail store that wants to increase sales on Tuesday and Wednesday,
# which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater,
# the store will discount the customer’s subtotal by 10%.

import os
from datetime import datetime

# Clear the console
os.system('cls')

set_discount = False

weekday = datetime.now().weekday()

def calculate_discount(subtotal_in):
    discount_percentage = 0.10
    discounted_subtotal = subtotal_in * discount_percentage
    return discounted_subtotal

def calcutate_tax(subtotal_in):
    tax = 0.06
    sales_tax_in = int(subtotal_in) * tax
    return sales_tax_in

# Checking if the subtotal is greater than or equal to $50 and if the weekday is Tuesday or Wednesday
def check_discount(subtotal_in,set_discount_in,weekday_in):
    check_day = False
    check_subtotal = False

    if subtotal_in >= 50:
        check_subtotal = True
        if weekday_in == 1 or weekday_in == 2:
            check_day = True
            if check_day and check_subtotal:
                set_discount_in = True
                return set_discount_in
    else:
        print("No discount applied.")

# Getting the subtotal
subtotal = int(input("Please enter the subtotal: "))

# Setting the discount if it is applicable
should_discount = check_discount(subtotal,set_discount,weekday)
discount = calculate_discount(subtotal)
if should_discount:
    print(f"Discount amount: {discount:.2f}")
    subtotal = subtotal - discount

sales_tax = calcutate_tax(subtotal)
print(f"Sales tax amount: {sales_tax:.2f}")

total_amount = subtotal + sales_tax
print(f"Total: {total_amount:.2f}")
