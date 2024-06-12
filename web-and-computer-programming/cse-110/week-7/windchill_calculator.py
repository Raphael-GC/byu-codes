#Author: Raphael Carneiro
# Week 7 Project: Windchill Calculator

import os
temperature = 'inf'

def calculate_wind_chill(temp, wind_speed):
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * wind_speed**0.16 + 0.4275 * temp * wind_speed**0.16
    return round(wind_chill, 2)

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return round(fahrenheit, 2)

def main(temp):
    global temperature
    unit = input("Fahrenheit or Celsius (F/C)? ").upper()

    if unit == "C":
        temp = convert_celsius_to_fahrenheit(temp)

    print(f"At temperature {temp}F, wind speeds and windchill values:")
    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temp, wind_speed)
        print(f"Wind speed {wind_speed} mph, the windchill is: {wind_chill}F")

    temperature = input("Press Enter to continue or type 'quit' to exit: ")

while True:
    if temperature != "quit":
        os.system("cls")
        temperature = float(input("What is the temperature? "))
        main(temperature)
    else:
        break
