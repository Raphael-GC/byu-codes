# Overview: This program is designed to help you practice writing basic functions.
# Instructions: 
# Write three functions:
# - display_regular—Receives a string and prints it out, exactly as received.
# - display_uppercase—Receives a string, converts it to upper case, and then prints it out.
# - display_lowercase—Receives a string, converts it to lower case, and then prints it out.


message = input("What is your message? ")

def display_regular(message):
    print(f"{message}")

def display_uppercase(message):
    print(f"{message.upper()}")

def display_lowercase(message):
    print(f"{message.lower()}")

display_regular(message)
display_uppercase(message)
display_lowercase(message)