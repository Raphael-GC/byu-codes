<h1 align="center">
    <img 
        alt="BYU-Idaho"
        title="BYU-Idaho Logo" 
        src="../.github/assets/logo-py.svg" 
        width="60%"
    />

Week 01 - Getting Started and Input/Output
</h1>
<b>Middle of Week Exercises:</b>

- [ID Badge Generator](/web-and-computer-programming/cse-110/week-1/id_badge_generator.py)
- [Clever Stories](/web-and-computer-programming/cse-110/week-1/clever_stories.py)

#### 💡📆 Tip of Week:
- Don't do this ! 🚫
```python
word = "The glory of GOD is intelligence."
print(f"The qty of letter G on the string is: {word.lower().count("g")}")
```

- Instead, make this ! ✅😁
```python
word = "The glory of GOD is intelligence."
qty = word.lower().count("g")
print(f"The qty of letter G on the string is: {qty}")
```
> It's even nicer and more readable.

#### 💡🤯 What did I learn this week?

>1. For large blocks of comments, we can start them with three "'s. Then we can type many lines of comments, and finish with three more "'s.
```python
    """
        Here's your comments.
    """
    # Also here's your comments.
```
---
>2. To assign a value to a variable using user input, we utilize the input() method.
```python
    # Ask for the basic information
    first = input("First name: ")
    last = input("Last name: ")
    email = input("Email address: ")
```
---
>3. String formatting has the following methods:
.lower() -> Makes the string completely lowercase.
.upper() -> Makes the string completely uppercase.
.title() -> Makes the first letter of each word in the string capitalized and the rest lowercase.
.capitalize() -> Makes the first letter of the string capitalized and the rest lowercase.

>There are also methods that return values ​​based on string formatting, for example:
.count("g") -> Returns the number of lowercase "g" letters in the string. Remembering that in this case, the method is case sensitive.

>To get the total amount of a letter, it is more appropriate to use it this way:
.lower().count("g") - Returns the number of letters "g" in the string, after making the entire string lowercase.

<br>

<div align="center">

<b>[Back](/web-and-computer-programming/cse-110/README.md)</b>

</div>

<img src="./../../../.github/assets/gradient-bar.svg" width="100%" height="8px"/>
<p align="center">Grow like a 🌳!</p>