# Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

# To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount
# and then multiply it by the fraction 5/9.

fahrenheit = float(input("What is the temperature in Fahrenheit? "))
celsius = f"{((fahrenheit - 32) * (5/9)):.1f}"
print(f"The temperature in Celsius is {celsius} degrees.")
