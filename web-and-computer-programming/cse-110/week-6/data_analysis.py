# Author: Raphael Carneiro
# Week 6 Project: Data Analysis
# Creativity Contributions:
# 1 - I added a menu for the user to select and filter results by year or country.
# 2 - I added a function to filter results by country and show the range of years searched.
# 3 - I added a function to filter results by continent  and show the range of years searched.

import os

entity = []
code = []
year = []
life_expectancy = []

with open("c:/Users/rapha/my-codes/byu-codes/web-and-computer-programming/cse-110/week-6/life_expectancy.csv", encoding='utf-8') as data_file:
    # getting information from each line in the file
    for index, line in enumerate(data_file):
        # skipping the first line
        if index == 0:
            continue

        # Braking the line after each comma. In this case, we have four columns [0][1][2][3].
        parts = line.strip().split(",")

        entity.append(parts[0])
        code.append(parts[1])
        year.append(int(parts[2]))
        life_expectancy.append(float(parts[3]))

parts2 = list(zip(entity, code, year, life_expectancy))

def overall_max(parts2_list):
    filtered_data = [register for register in parts2_list if register[1] != '']

    if not filtered_data:
        print("No data found.")
        return

    max_life = max(filtered_data, key=lambda x: x[3])

    print(f"The overall max life expectancy is: {max_life[3]} from {max_life[0]} in {max_life[2]}")

def overall_min(parts2_list):
    filtered_data = [register for register in parts2_list if register[1] != '']

    if not filtered_data:
        print("No data found.")
        return

    min_life = min(filtered_data, key=lambda x: x[3])

    print(f"The overall max life expectancy is: {min_life[3]} from {min_life[0]} in {min_life[2]}")

def search_max_min_avg(parts2_list, year_searched):
    filtered_data = [register for register in parts2_list if register[2] == year_searched]

    if not filtered_data:
        print(f"No data found for the year {year_searched}")
        return

    min_life = min(filtered_data, key=lambda x: x[3])
    max_life = max(filtered_data, key=lambda x: x[3])
    sum_life = sum(register[3] for register in filtered_data)
    avg_life = sum_life / len(filtered_data)

    print(f"The average life expectancy across all countries (234) in {year_searched} was {avg_life:.2f}")
    print(f"The min life expectancy was in {min_life[0]} with {min_life[3]} in {year_searched}")
    print(f"The max life expectancy was in {max_life[0]} with {max_life[3]} in {year_searched}")

def search_year():
    os.system("cls")
    year_searched = int(input("🔍 Enter the year of interest: "))
    print()
    overall_max(parts2)
    overall_min(parts2)
    print()
    print(f"For the year {year_searched}:")
    print()
    search_max_min_avg(parts2, year_searched)

def search_country(parts2_list):
    os.system("cls")
    country_searched = input("Enter the country of interest: ")
    filtered_data = [register for register in parts2_list if register[0].lower() == country_searched.lower()]

    min_life = min(filtered_data, key=lambda x: x[3])
    max_life = max(filtered_data, key=lambda x: x[3])
    sum_life = sum(register[3] for register in filtered_data)
    avg_life = sum_life / len(filtered_data)

    print(f"The average life expectancy for {country_searched.title()} was {avg_life:.2f}")
    print(f"The min life expectancy was {min_life[3]} in {min_life[2]}")
    print(f"The min life expectancy was {max_life[3]} in {max_life[2]}")
def search_continent(parts2_list, continent_searched):
    os.system("cls")
    filtered_data = [register for register in parts2_list if register[0].lower() == continent_searched.lower()]

    min_life = min(filtered_data, key=lambda x: x[3])
    max_life = max(filtered_data, key=lambda x: x[3])
    sum_life = sum(register[3] for register in filtered_data)
    avg_life = sum_life / len(filtered_data)

    print(f"The average life expectancy for {continent_searched.title()} was {avg_life:.2f}")
    print(f"The min life expectancy was {min_life[3]} in {min_life[2]}")
    print(f"The min life expectancy was {max_life[3]} in {max_life[2]}")

def menu_continent():
    os.system("cls")
    continent_searched = ''

    while True:
        print()
        print("1. Americas")
        print("2. Africa")
        print("3. Asia")
        print("4. Europe")
        print("5. Northern America")
        print("6. Oceania")
        print("7. 🔙 Main Menu\n")
        try:
            choice2 = int(input("Enter the continent of interest (type a number): "))
        except ValueError:
            print("Please enter a valid choice.")
            continue
        if choice2 == 1:
            continent_searched = "africa"
            search_continent(parts2, continent_searched)
        elif choice2 == 2:
            continent_searched = "americas"
            search_continent(parts2, continent_searched)
        elif choice2 == 3:
            continent_searched = "asia"
            search_continent(parts2, continent_searched)
        elif choice2 == 4:
            continent_searched = "europe"
            search_continent(parts2, continent_searched)
        elif choice2 == 5:
            continent_searched = "northern america"
            search_continent(parts2, continent_searched)
        elif choice2 == 6:
            continent_searched = "oceania"
            search_continent(parts2, continent_searched)
        elif choice2 == 7:
            print()
            break
        else:
            print("Please enter a valid choice.\n")
            continue

while True:
    print()
    print("🔍 Research life expectancy around the world!🔎")
    print()
    print("1. Search by YEAR")
    print("2. Search by COUNTRY")
    print("3. Search by CONTINENT")
    print("4. 🔚 Quit")
    try:
        choice = int(input("Please enter an action: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue
    if choice == 1:
        search_year()
    elif choice == 2:
        search_country(parts2)
    elif choice == 3:
        menu_continent()
    elif choice == 4:
        print("\nThank you. Goodbye.👋🏾 ")
        break
    else:
        print("Please enter a valid choice.")
        continue
