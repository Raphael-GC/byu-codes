# Overview: Write functions to compute and return the areas of squares, rectangles, and circles. 
# These functions should not display the values directly, but rather should return them, so they could be used in other parts of the program.

import math, os

def compute_area_square(side):
    area_of_square = side * side
    return area_of_square

def compute_area_rectangle(length, width):
    area_rectangle = length * width
    return area_rectangle
def compute_area_circle(radius):
    area_of_circle = math.pi * radius ** 2
    return area_of_circle

while True:
    print("\n🧮 Area Calculator 🧮")
    print()
    print("What Area would you like to Calculate?")
    print("1. ◽ Square")
    print("2. ➖ Rectangle")
    print("3. 🔘 Circle")
    print("4. 🔚 Quit")
    try:
        choice = int(input("Please enter an action: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue
    if choice == 1:
        side_square = float(input('What is the lenght of a side of the square? '))
        os.system('cls')
        print(f"The area of Square is: {compute_area_square(side_square):.2f}")
    elif choice == 2:
        length_rectangle = float(input('What the length of the rectangle? '))
        width_rectangle = float(input('What the width of the rectangle? '))
        os.system('cls')
        print(f"The area of Rectangle is: {compute_area_rectangle(length_rectangle, width_rectangle):.2f}")
    elif choice == 3:
        radius = float(input('What is the radius of the circle? '))
        os.system('cls')
        print(f"The area of Circle is: {compute_area_circle(radius):.2f}")
    elif choice == 4:
        os.system('cls')
        print("\nThank you. Goodbye.👋🏾 ")
        break
