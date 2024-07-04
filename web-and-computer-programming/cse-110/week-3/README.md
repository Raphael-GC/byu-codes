<h1 align="center">
    <img 
        alt="BYU-Idaho"
        title="BYU-Idaho Logo" 
        src="../.github/assets/logo-py.svg" 
        width="60%"
    />

Week 03 - Decisions
</h1>
<b>Middle of Week Exercises:</b>

- [Comparing Numbers and Strings](/web-and-computer-programming/cse-110/week-3/comparing_numbers_and_strings.py)
- [Qualifying for a Loan](/web-and-computer-programming/cse-110/week-3/qualifying_for_a_loan.py)

#### 💡📆 Tips of Week:

>Common boolean variable names are: is_xxx, has_xxx, can_xxx, should_xxx, etc.
---
- Don't do this ! 🚫
```python
    # To check if x is either 5 or 6, you might be tempted to write:
    if x == 5 or 6:
    # INCORRECT: This does not work!
```

- Instead, make this ! ✅😁
```python
    # You must write them both out:
    if x == 5 or x == 6:
    # This is the correct way to check
```
[Week's Project: Adventure Game](/web-and-computer-programming/cse-110/week-3/adventure_game.py) <br><br>
[Team Activity: Area of Shapes](/web-and-computer-programming/cse-110/week-3/team_project_area_of_shapes.py)

#### 💡🤯 What did I learn this week?

>1. This week, while I prepared for a team activity and compared my code with the sample solution. I realized how redundant my code was and was amazed that I had used three times more lines than necessary to fulfill the requirements. I learned my lesson and will analyze all possibilities for reducing my code in the future.
---
>2. `Testing Multiple Conditions`: Just as mathematical operators have precedence rules where * happens before +, the and condition takes precedence over the or condition, so if you want to mix them and have the or condition happen first, you need to use parentheses:
```python
    if (x > 5 or x < -5) and y > 10:
    # In this case, x can either be greater than 5 or less than negative 5, and y must
    # always be greater than 10

    if x > 5 or x < -5 and y > 10:
    # Without parentheses, the x < -5 and y > 10 conditions go together and both must be
    # true, unless x > 5, in which case the whole statement is true
```
---
>3. `True and False values`: You can set a boolean variable directly, such as is_hot = True or is_hot = False. Notice that you must always use a capital T on True and a capital F on False.
```python
    is_hot = True

    # You can check the value of the variable directly
    if is_hot:
    print("It's hot")

    # It works, but is redundant (and therefore bad practice) to check if it is True:
    if is_hot == True:
    print("It's hot")
```

<br>

<div align="center">

<b>[Back](/web-and-computer-programming/cse-110/README.md)</b>

</div>

<img src="./../../../.github/assets/gradient-bar.svg" width="100%" height="8px"/>
<p align="center">Grow like a 🌳!</p>