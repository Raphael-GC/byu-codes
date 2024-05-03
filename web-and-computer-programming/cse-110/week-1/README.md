<h1 align="center">
    <img 
        alt="BYU-Idaho"
        title="BYU-Idaho Logo" 
        src="../.github/assets/logo-py.svg" 
        width="60%"
    />

Week 01 - Getting Started and Input/Output
</h1>

### Code 1 : 
Author: Brother Burton
Purpose: Display text to the screen.

<details>
    <summary>Sample solution</summary>

    ```python
    color = input('What is your favorite color? ')
    print('Your favorite color is')
    print(color)

    # Please note that you can use either single quotes: 'Your favorite color is' or double
    # quotes: "Your favorite color is" in your print and inputs statements and it will work
    # just fine. It is completely a programmer preference.

    # Lines that start with a "#" like this one are called "comments" and don't have
    # code that actually runs. Instead, they allow us to make notes in our programs
    # for other programmers to see.

    """
    For large blocks of comments, we can start them with three "'s.
    then we can type many lines of comments, and finish with three more "'s.
    These are a special kind of comment that you'll learn more about later on.
    """
    ```
</details>

### Code 2 : 
Author: Brother Burton
Purpose: Display text to the screen.

<details>
    <summary>Sample solution</summary>

    ```python
    first = input("What is your first name? ")
    last = input("What is your last name? ")

    # This is for the the first part of the activity
    print(f"Your name is {last}, {first} {last}.")

    # This is for the the second part, where we adjust the capitalization
    print(f"Your name is {last.title()}, {first.title()} {last.title()}.")

    # Be aware that there are many ways to do the formatting of that line, such as:
    # print("Your name is " + last + ", " + first + " " + last + ".")
    # print("Your name is {}, {} {}.".format(last, first, last))
    # print("Your name is {0}, {1} {0}.".format(last, first))
    ```
</details>

### Code 3 : 
Author: Brother Burton
Purpose: Practice formatting strings.
This program also contains a way to implement the stretch challenges.

<details>
    <summary>Sample solution</summary>

    ```python
    print("Please enter the following information:")

    print()

    # Ask for the basic information
    first = input("First name: ")
    last = input("Last name: ")
    email = input("Email address: ")
    phone = input("Phone number: ")
    job_title = input("Job title: ")
    id_number = input("ID Number: ")

    # Ask for the additional information
    hair_color = input("Hair color: ")
    eye_color = input("Eye color: ")
    month = input("Starting Month: ")
    training = input("Completed additional training? ")

    # Now print out the ID Card
    print("\nThe ID Card is:")
    print("----------------------------------------")
    print(f"{last.upper()}, {first.capitalize()}")
    print(job_title.title())
    print(f"ID: {id_number}")
    print()
    print(email.lower())
    print(phone)
    print()

    # There are various ways to accomplish the spacing

    # In this approach, I told it that hair_color will take exactly 15
    # spaces, and month will take 14. That way, the next columns will
    # line up. I had to do month 14 (instead of 15) because the word
    # 'Month' that came before my value was one letter longer.

    print(f"Hair: {hair_color:15} Eyes: {eye_color}")
    print(f"Month: {month:14} Training: {training}")
    print("----------------------------------------")
    ```
</details>

### Code 4 : 
Purpose: Write a program with variables and strings to accomplish a meaningful task.
Task: Complete the requirements for your program.

<center>

<b>[Back](/web-and-computer-programming\cse-110\README.md)</b>

<img src="./../../../.github/assets/gradient-bar.svg" width="100%" height="8px"/>
<p align="center">Grow like a 🌳!</p>