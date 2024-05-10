# Team Activity - Grade Calculator Program
# Instructions: Write a program that determines the letter grade for a course.

# Core Requirements 
"""
grade = int(input("Enter your grade percentage from 0-100: "))
letter_grade = "F"

if grade >= 90:
    letter_grade =  "A"
    print(f"Your letter grade is {letter_grade}.\nCongratulations, you have been approved! 🥳")
elif grade >= 80:
    letter_grade = "B"
    print(f"Your letter grade is {letter_grade}.\nCongratulations, you have been approved! 🥳")
elif grade >= 70:
    letter_grade = "C"
    print(f"Your letter grade is {letter_grade}.\nCongratulations, you have been approved! 🥳")
elif grade >= 60:
    letter_grade = "D"
    print(f"Your letter grade is {letter_grade}.\nCongratulations, you have been approved! 🥳")
else:
    print(f"Your letter grade is {letter_grade}.\n😞 You haven't been approved. \nTry to do your best next term!")
"""

# Stretch Challenge
grade = int(input("Enter your grade percentage from 0-100: "))
letter_grade = "F"
sign_grade = "-"

if grade >= 90:
    letter_grade =  "A"
    if grade >= 93:
        print(f"Your letter grade is {letter_grade}.🥳\nCongratulations, you have been approved! 🥳")
    else:
        print(f"Your letter grade is {letter_grade}{sign_grade}.\nCongratulations, you have been approved! 🥳")
elif grade >= 80:
    letter_grade =  "B"
    if grade >= 87:
        sign_grade = "+"
        print(f"Your letter grade is {letter_grade}{sign_grade}.\nCongratulations, you have been approved! 🥳")
    elif grade >= 83:
        print(f"Your letter grade is {letter_grade}.\nCongratulations, you have been approved! 🥳")
    else:
        print(f"Your letter grade is {letter_grade}{sign_grade}.\nCongratulations, you have been approved! 🥳")
elif grade >= 70:
    letter_grade = "C"
    if grade >= 77:
        sign_grade = "+"
        print(f"Your letter grade is {letter_grade}{sign_grade}.\nCongratulations, you have been approved! 🥳")
    elif grade >= 73:
        print(f"Your letter grade is {letter_grade}.\nCongratulations, you have been approved! 🥳")
    else:
        print(f"Your letter grade is {letter_grade}{sign_grade}.\nCongratulations, you have been approved! 🥳")
elif grade >= 60:
    letter_grade = "D"
    if grade >= 67:
        sign_grade = "+"
        print(f"Your letter grade is {letter_grade}{sign_grade}.\n😞 You haven't been approved. \nTry to do your best next term!")
    elif grade >= 63:
        print(f"Your letter grade is {letter_grade}.\n😞 You haven't been approved. \nTry to do your best next term!")
    else:
        print(f"Your letter grade is {letter_grade}{sign_grade}.\n😞 You haven't been approved. \nTry to do your best next term!")
else:
    print(f"Your letter grade is {letter_grade}.\n😞 You haven't been approved. \nTry to do your best next term!")
