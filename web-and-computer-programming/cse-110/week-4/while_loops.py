# Write a Python Program that does each of the following:

# 1. Use a while loop to ask the user for a positive number (>= 0).
# Continue asking as long as the number is negative, then display the number. For example:

# 2. Use a while loop, to simulate a child asking their parent for a piece of candy.
# Have the program keep looping until the user answers "yes", then have the program output "Thank you." For example:

# CHALLENGE #1
number = -1
while number < 0:
    number = int(input("Please type a positive number: "))
    if number >= 0:
        checked_number = int(number)
        print(f"The number is: {checked_number}")
        break
    elif number < 0:
        print("Sorry, that is a negative number. Please try again.")

# CHALLENGE #2
child_answer = ""
while child_answer.lower()!= "yes":
    child_answer = input("Do you want some candy? (yes/no): ")
    if child_answer.lower() == "yes":
        print("Thank you.")
