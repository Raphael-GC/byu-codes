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
    print(vehicle_type)
    if  vehicle_type.lower == "car":
        car_catalog.append(line)
    elif vehicle_type.lower == "motocycle":
        motocycle_catalog.append(line)

print(car_catalog[0])
print()
print(motocycle_catalog[0])
