# Author: Raphael Carneiro
# Week 01 - Prove: Tire Volume
# Core Requirements: ✅
# Exceeding the Requirements: ✅

import math
import os
from datetime import datetime

os.system('cls')

# Initializing the lists to store data from the CSV file
tire_type = []
width = []
aspect_ratio = []
diameter = []
price = []
tire_name = []
found_tires = []
width_match = []

# Opening the CSV file and reading the data
with open("c:/Users/rapha/my-codes/byu-codes/web-and-computer-programming/cse-111/week-1/tires.csv", encoding='utf-8') as data_file:
    # getting information from each line in the file
    for index, line in enumerate(data_file):
        # skipping the first line
        if index == 0:
            continue

        # Braking the line after each comma. In this case, we have six columns [0][1][2][3][4][5].
        parts = line.strip().split(",")

        # Save each part into a especific list
        tire_type.append(parts[0])
        width.append(int(parts[1]))
        aspect_ratio.append(int(parts[2]))
        diameter.append(int(parts[3]))
        price.append(int(parts[4]))
        tire_name.append(parts[5])

# Gathering all lists in a tuple
general_catalog = list(zip(tire_type,width,aspect_ratio,diameter,price,tire_name))

# Separating the general catalog into car and motocycle catalogs
car_catalog = []
motocycle_catalog = []
for line in general_catalog:
    vehicle_type = line[0]
    if  vehicle_type.lower == "car":
        car_catalog.append(line)
    else:
        motocycle_catalog.append(line)

# Calculate the volume, print and store the result in volumes.txt - Core Requirements ✅
def only_calculate_volume():
    today = datetime.now().today()
    user_width = int(input("Enter the width of the tire in mm (145 - 355): "))
    user_aspect_ratio = int(input("Enter the aspect ratio of the tire in % (25 - 85): "))
    user_diameter = int(input("Enter the diameter of the wheel in inches (13 - 24): "))

    user_volume = (math.pi * user_width**2 * user_aspect_ratio * (user_width * user_aspect_ratio + 2540 * user_diameter)) / 10000000000
    print(f"The approximate volume is {user_volume:.2f} liters")

    with open("c:/Users/rapha/my-codes/byu-codes/web-and-computer-programming/cse-111/week-1/volumes.txt", 'at', encoding='utf-8') as tire_file:
        print(f"{today:%Y-%m-%d}, {user_width}, {user_aspect_ratio}, {user_diameter}, {user_volume:.2f}", file=tire_file)

# Function to help the users to find the ideal tire for their vehicle through width, aspect ratio or diameter.
def motocycle_tire():
    print()
    print("🏍️ Let's check some tire informations! 🏍️")
    print()

    while True:
        print()
        print("Choose a tire characteristic to find your ideal tire:")
        print("1. Width")
        print("2. Aspect Ratio")
        print("3. Diameter")
        print("4. 🔙 Back to tire type selection")
        print()
        try:
            characteristic_choice = int(input("Please enter an action: "))
        except ValueError:
            print("Please enter a valid choice.")
            continue
        if characteristic_choice == 1:
            user_width = int(input("Enter the width of the tire in mm (60 - 240): "))
            if 60 <= user_width <= 40:
                closest_indx = find_closest_indices(width, user_width)
                printing_tires (closest_indx, motocycle_catalog)
            else:
                print(f"The width {width} mm is not within the valid range.")
        elif characteristic_choice == 2:
            user_aspect_ratio = int(input("Enter the aspect ratio of the tire in % (30 - 90): "))
            if 30 <= user_aspect_ratio <= 90:
                closest_indx = find_closest_indices(aspect_ratio, user_aspect_ratio)
                printing_tires (closest_indx, motocycle_catalog)
            else:
                print(f"The aspect ratio {user_aspect_ratio}% is not within the valid range.")
        elif characteristic_choice == 3:
            user_diameter = int(input("Enter the diameter of the wheel in inches (10 - 21): "))
            if 10 <= user_diameter <= 21:
                closest_indx = find_closest_indices(diameter, user_diameter)
                printing_tires (closest_indx, motocycle_catalog)
            else:
                print(f"The diameter {user_diameter} inches is not within the valid range.")
        elif characteristic_choice == 4:
            break
        else:
            print("Please enter a valid choice.")
            continue

# Function to help the users to find the ideal tire for their vehicle through width, aspect ratio or diameter.
def car_tire():
    print()
    print("🚗 Let's check some tire informations! 🚗")
    print()

    while True:
        print()
        print("Choose a tire characteristic to find your ideal tire:")
        print("1. Width")
        print("2. Aspect Ratio")
        print("3. Diameter")
        print("4. 🔙 Back to tire type selection")
        print()
        try:
            characteristic_choice = int(input("Please enter an action: "))
        except ValueError:
            print("Please enter a valid choice.")
            continue
        if characteristic_choice == 1:
            user_width = int(input("Enter the width of the tire in mm (145 - 355): "))
            if 145 <= user_width <= 355:
                closest_indx = find_closest_indices(width, user_width)
                printing_tires (closest_indx, car_catalog)
            else:
                print(f"The width {width} mm is not within the valid range.")
        elif characteristic_choice == 2:
            user_aspect_ratio = int(input("Enter the aspect ratio of the tire in % (25 - 85): "))
            if 25 <= user_aspect_ratio <= 85:
                closest_indx = find_closest_indices(aspect_ratio, user_aspect_ratio)
                printing_tires (closest_indx, car_catalog)
            else:
                print(f"The aspect ratio {user_aspect_ratio}% is not within the valid range.")
        elif characteristic_choice == 3:
            user_diameter = int(input("Enter the diameter of the wheel in inches (13 - 24): "))
            if 13 <= user_diameter <= 24:
                closest_indx = find_closest_indices(diameter, user_diameter)
                printing_tires (closest_indx, car_catalog)
            else:
                print(f"The diameter {user_diameter} inches is not within the valid range.")
        elif characteristic_choice == 4:
            break
        else:
            print("Please enter a valid choice.")
            continue

# Function to search for the closest values in tne especific list
def find_closest_indices(numbers, target):
    closest_indices = []
    min_difference = float('inf')

    for i, number in enumerate(numbers):
        difference = abs(number - target)

        if difference < min_difference:
            min_difference = difference
            closest_indices = [i]  # Start a new list for the closest index
        elif difference == min_difference:
            closest_indices.append(i)  # Add this index if it's equally close

    return closest_indices

# Function to printing on the screen the ideal tires and ask the users if they want to buy them and save the name and phone number in csv file
def printing_tires (indices, tire_catalog):
    today = datetime.now().today()
    line_response = 1
    print()
    print("We assume that these tires will fulfill your requirements: ")
    for i in indices:
        print(f"{line_response}. {tire_catalog[i][0]}, {tire_catalog[i][1]}mm, {tire_catalog[i][2]}%, {tire_catalog[i][3]}R, ${tire_catalog[i][4]}, {tire_catalog[i][5]}")
        line_response = line_response + 1

    while True:
        print()
        print("Would you like to buy some of them?")
        print("1. Yes")
        print("2. 🔙 No and Back to previuos menu")
        print("3. 🔚 No and Quit")
        try:
            print()
            choice = int(input("Please enter an action: "))
        except ValueError:
            print("Please enter a valid choice.")
            continue
        if choice == 1:
            print()
            customer_name = input("Please enter your name: ").title()
            customer_number = str(input("Please enter your phone number: "))
            print()
            print("Thank you for you interest in purchase them! We'll contact you soon.")
            for i in indices:
                with open("c:/Users/rapha/my-codes/byu-codes/web-and-computer-programming/cse-111/week-1/costumers.csv", 'at', encoding='utf-8') as tire_file:
                    print(f"{today:%Y-%m-%d}, {customer_name}, {customer_number}, {tire_catalog[i][0]}, {tire_catalog[i][1]}, {tire_catalog[i][2]}, {tire_catalog[i][3]}, {tire_catalog[i][4]}, {tire_catalog[i][5]}", file=tire_file)
            break
        elif choice == 2:
            print("\nReturning to the previous menu...\n")
            motocycle_tire()
        elif choice == 3:
            print("\nThank you. Goodbye.👋🏾 ")
            break
        else:
            print("Please enter a valid choice.")
            continue

# Main menu
def main():
    while True:
        print()
        print("🚗 What kind of tire are you looking for? 🏍️")
        print()
        print("1. CAR tire 🚗")
        print("2. MOTORCYCLE tire 🏍️")
        print("3. 🔚 Quit")
        print()
        try:
            choice = int(input("Please enter an action: "))
        except ValueError:
            print("Please enter a valid choice.")
            continue
        if choice == 1:
            os.system('cls')
            car_tire()
        elif choice == 2:
            os.system('cls')
            motocycle_tire()
        elif choice == 3:
            only_calculate_volume()
        elif choice == 4:
            print("\nThank you. Goodbye.👋🏾 ")
            break
        else:
            print("Please enter a valid choice.")
            continue

main()
