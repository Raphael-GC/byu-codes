# Author: Raphael Carneiro
# Week 6 Project: Data Analysis
# Creativity Contributions: 
# 1 - I added a menu for the user to select and filter results by year or country.
# 2 - I added a function to filter results by country.
# 3 - I added a function to filter results by continent.

import os
os.system('cls')

entity = []
code = []
year = []
life_expectancy = []

with open("c:/Users/rapha/my-codes/byu-codes/web-and-computer-programming/cse-110/week-6/life_expectancy.csv") as data_file:
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

def overall_max(parts, life_expectancy):
    max_life = -1
    for life_expectancy in enumerate(parts):
        if float(parts[3]) == max(life_expectancy):
            max_life = float(parts[3])
            max_year = int(parts[2])
            max_entity = parts[0]
            print(f"The overall max life expectancy is: {max_life} from {max_entity} in {max_year}")
    
def overall_min(parts, life_expectancy):
    min_life = 999999
    for life_expectancy in enumerate(parts):       
        if float(parts[3]) == min(life_expectancy):
            min_life = float(parts[3])
            min_year = int(parts[2])
            min_entity = parts[0]
            print(f"The overawll min life expectancy is: {min_life} from {min_entity} in {min_year}")

def search_max_life(entity, life_expectancy, year, year_searched):
    max_life = -1
    results = []

    for i in range(len(year)):
        if year[i] == year_searched:
            if life_expectancy[i] > max_life:
                max_life = life_expectancy[i]
                results = [(entity[i], year[i], life_expectancy[i])]
            #elif life_expectancy[i] == max_life:
                #results.append((entity[i], year[i], life_expectancy[i]))
            else:
                continue
        else:
            continue
    
    if results:
        print(f"The max life expectancy was in {results[0]} with {results[2]}")
    else:
        print(f"No data found for the year {year_searched}")

def search_min_life(entity, life_expectancy, year, year_searched):
    min_life = 999999
    results = []    

    for i in range(len(year)):
        if year[i] == year_searched:
            if life_expectancy[i] < min_life:
                min_life = life_expectancy[i]
                results = [(entity[i], year[i], life_expectancy[i])]
            #elif life_expectancy[i] == min_life:
                #results.append((entity[i], year[i], life_expectancy[i]))
            else:
                continue
        else:
            continue
    
    if results:
        print(f"The min life expectancy was in {results[0]} with {results[2]}")
    else:
        print(f"No data found for the year {year_searched}")

def average_life(entity, life_expectancy, year, code, year_searched):
    average = 0
    results = []

    for i in range (len(entity)):    
        if code != '':
            if year == year_searched:
                results.append(float(life_expectancy[i]))
            else:
                continue
        else:
            continue
    
    for i in range(len(results)):
        average += results[i]
        
    average = average / len(results)
    
    print(f"The average life expectancy across all countries was {average}")

def search_year(parts, entity, year,life_expectancy):
    os.system("cls")
    year_searched = int(input("🔍 Enter the year of interest: \n"))

    overall_max(parts, life_expectancy)
    overall_min(parts, life_expectancy)
    print()
    print(f"For the year {year_searched}:")
    average_life(entity, life_expectancy, year, code, year_searched)
    search_max_life(entity, year, life_expectancy, year_searched)
    search_min_life(entity, year, life_expectancy, year_searched)
           
while True:
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
        search_year(parts, entity, year,life_expectancy)
    elif choice == 2:
        search_country()
    elif choice == 3:
        search_continent()
    elif choice == 4:
        print("\nThank you. Goodbye.👋🏾 ")
        break
    else:
        print("Please enter a valid choice.")
        continue