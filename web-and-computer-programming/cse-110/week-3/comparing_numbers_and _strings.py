# Activity Instructions:
# Practice writing programs that compare strings and numbers.

# Getting and Comparing Numbers
first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

if first_number > second_number:
    print("\nThe first number is greater")
else:
    print("\nThe first number is not greater")

if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if first_number < second_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

# Getting and Comparing Strings, regardless of the captalization
animal = input("\nWhat is your favorite animal? ")

if animal.lower() == "tiger":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
