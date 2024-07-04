# Write a Python Program that does each of the following:

#Given the following list of items:
colors = ["red", "blue", "green", "yellow"]

# 1. Use a for loop to iterate through this list one by one and display each item on its own line.
# 2. Use a for loop to display the numbers 1–8, one number on each line.
# 3. Use a for loop to display the even numbers (hint: count by two) 2–20, one number on each line.

# CHALLENGE #1
for color in colors:
    print(color)

print()
# CHALLENGE #2
for i in range(1, 9):
    print(i)

print()
# CHALLENGE #3
for i in range(2, 21, 2):
    print(i)
