# Write a program that does the following:

# 1. Prompt the user for their age.
# Convert it to a number, add one to it, and tell them how old they will be on their next birthday.

# 2. Prompt the user for the number of egg cartons they have.
# Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

# 3. Prompt the user for a number of cookies and a number of people.
# Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

years_old = int(input("How old are you? "))
print(f"On your next birthday, you will be {years_old + 1}")

egg_cartoons = int(("How many egg cartons do you have? "))
print(f"You have {egg_cartoons * 12} eggs")

cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
portion = float(cookies / people)
print(f"Each person may have {portion:.2f} cookies")

# Note: This program assumes that the user will input valid numbers for age, egg cartons, cookies, and people.
