<h1 align="center">
    <img 
        alt="BYU-Idaho"
        title="BYU-Idaho Logo" 
        src="../.github/assets/logo-py.svg" 
        width="60%"
    />

Week 02 - Variables and Expressions
</h1>
<b>Middle of Week Exercises:</b>

- [Numeric Variables](/web-and-computer-programming/cse-110/week-2/numeric_variables.py)
- [Mathematical Expressions](/web-and-computer-programming/cse-110/week-2/mathematical_expressions.py)

#### 💡📆 Tip of Week:
- Don't do this ! 🚫
```python
    price = 123.456
    print(f"{price:.2f}")
```

- Instead, make this ! ✅😁
```python
    price = 123.456
    formatted_price = f"{price:.2f}"
    print(formatted_price)
```
> It's even nicer and more readable.

[Week's Project: Meal Price Calculator](/web-and-computer-programming/cse-110/week-2/meal_price_calculator_final.py)
[Team Activity: Grade Calculator Program](/web-and-computer-programming/cse-110/week-2/team_activity.py)

- [my solution](/web-and-computer-programming/cse-110/week-2/team_project_grade_calculator_program.py)
- [sample solution](/web-and-computer-programming/cse-110/week-2/team_grades_stretch_sample.py)

#### 💡🤯 What did I learn this week?

>1. When displaying floating values, we can limit the number of decimal places after the decimal point using the following format: price:.2f

In this format:
- `price` is the variable that holds the numeric value we want to format.
- `:` separates the variable we want to format from the format specification.
- `.2f` specifies the number of decimal places after the decimal point:
   - The period `.` indicates that we are specifying the number of decimal places.
   - The number `2` represents the number of decimal places we want after the decimal point.
   - The letter `f` indicates that we are formatting a floating point number (float).
```python
    price = 123.456
    formatted_price = f"{price:.2f}"
    print(formatted_price)
    ---
    # Output: 123.46
```
---
>2. If you want to use integer values in strings, you CANNOT just add them, you first have to convert them to a string:
- WRONG:
```python
    print("Twice as many is: " + double_number)
```
- RIGHT:
```python
    double_string = str(double_number)
    print("Twice as many is: " + double_string)
```
- Also RIGHT:
```python
    print("Twice as many is " + str(double_number))
```
---
>3. Math Library: Rounding a number.
- [Mathematical functions](https://docs.python.org/3/library/math.html) There are lots of things available in the math library.
    - `math.ceil(value)`—Rounds value up to the next whole number, the "ceiling."

    - `math.floor(value)`—Rounds value down to the next whole number.

    - `math.exp(value)`—Raises e to the power of value.

    - `math.sin(value)`—Computes the trigonometry sine function of value in radians.
```python
    import math

    weight = 1.65

    lower = math.floor(weight)
    print(lower)
    # Output: 1

    higher = math.ceil(weight)
    print(higher)
    # Output: 2
```

<br>

<div align="center">

<b>[Back](/web-and-computer-programming/cse-110/README.md)</b>

</div>

<img src="./../../../.github/assets/gradient-bar.svg" width="100%" height="8px"/>
<p align="center">Grow like a 🌳!</p>