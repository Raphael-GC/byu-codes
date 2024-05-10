# Code made with the class
grade = int(input("Please insert your grade: "))

# Getting grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Stretch Challenge 1 
remainder = grade % 10
if remainder >= 7:
    sign = "+"
elif remainder <= 3:
    sign = "-"
else:
    sign = ""

# Stretch Challenge 2
if remainder >= 7 and letter == "A":
    sign = ""
# Stretch Challenge 3
elif remainder >= 7 and letter == "F":
    sign = ""
elif remainder <= 3 and letter == "F":
    sign = ""


print(f"Your letter is {letter}{sign}")
if grade >= 70:
    print("Congratulations!! You pass the class!")
else:
    print("Sorry, but you have to try hard next year!")
    