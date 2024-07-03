# Overview: Practice creating lists, adding to them, and iterating through them.

import os

name_list = []
name_checker = 'inf'

# Add names to the list
while name_checker != 'end':
    name_checker = input("Type the name of a friend: ")
    if name_checker!= 'end':
        name_list.append(name_checker)

# Print the list of names
os.system('cls')
print("Your friends are:")
for name in name_list:
    print(name)