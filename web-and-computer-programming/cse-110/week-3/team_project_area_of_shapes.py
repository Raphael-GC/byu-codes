#Group18
#For the stretch activity, we imported the math package and rounded the area of the circle
#We also ask for 1 length and use it compute multiple values 
import math

#Area of Square
length_of_side = float(input('What is the lenght of a side of the square? '))
area_of_square = length_of_side * length_of_side
print(f'The area of the square is: {area_of_square:.2f}')
print()

#Length and area of rectange
base_rectangle = float(input('What the base of the rectangle? '))
height_rectangle = float(input('What the height of the rectangle? '))
area_rectangle = base_rectangle * height_rectangle
print(f'The area of rectangle is {area_rectangle:.2f}')
print()
                              
#Radius of the circle
radius = float(input('What is the radius of the circle? '))
area_of_circle = math.pi * radius ** 2
print(f'The area of the circle is: {area_of_circle:.2f}')
print()

#single length computes area of square, circle, volume of cube, and volume of sphere
length = float(input('Please enter a length '))
area_of_square = length ** 2
area_of_circle = math.pi * length ** 2
volume_of_cube = length ** 3
volume_of_sphere = 4/3 * math.pi * length ** 3
print(f'The area of the square is {area_of_square:.2f}')
print(f'The area of the circle is {area_of_circle:.2f}')
print(f'The volume of the cube is {volume_of_cube:.2f}')
print(f'The volume of the sphere is {volume_of_sphere:.2f}')

#Change the prompt to ask for centimeters
#This section is not complete

#Area of Square in centimeters
# length_of_side = float(input('What is the lenght of a side of the square in centimeters? '))
# area_of_square_in_centimeters = length_of_side * length_of_side
# area_of_square_in_meters = length_of_side * length_of_side * 1/10000
# print(f'The area of the square in centimeters is: {area_of_square_in_centimeters:.2f}')
# print(f'The area of the square in meters is: {area_of_square_in_meters:.2f}')

# #Length and area of rectange in centimeters
# base_rectangle = float(input('What the base of the rectangle? '))
# height_rectangle = float(input('What the height of the rectangle? '))
# area_rectangle = base_rectangle * height_rectangle
# print(f'The area of rectangle is {area_rectangle:.2f}')
                                   
#Radius of the circle in centimeters
# radius = float(input('What is the radius of the circle? '))
# area_of_circle = math.pi * radius ** 2
# print(f'The area of the circle is: {area_of_circle:.2f}')
