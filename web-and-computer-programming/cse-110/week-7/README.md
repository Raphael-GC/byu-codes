<h1 align="center">
    <img 
        alt="BYU-Idaho"
        title="BYU-Idaho Logo" 
        src="../.github/assets/logo-py.svg" 
        width="60%"
    />

Week 07 - Functions
</h1>
<b>Middle of Week Exercises:</b>

- [Recieve + Modify + Print](/web-and-computer-programming/cse-110/week-7/display_string.py)
- [Area Calculator](/web-and-computer-programming/cse-110/week-7/area_calculator.py)

#### 💡📆 Tip of Week:
- Don't do this ! 🚫
```python
import datetime
print(datetime.datetime.now())
```

- Instead, make this ! ✅😁
```python
from datetime import datetime
print(datetime.now())
```
> It's even nicer and more readable.

<b>

[Week's Project: ](/web-and-computer-programming/cse-110/week-7/windchill_calculator.py) </b><br><br>

#### 💡🤯 What did I learn this week?

>1. We can get the first position of a string, as it were a list, this way:
```python
name = "Raphael"
name_initial = name[0:1]
```
---
>2. When you use named parameters, you can specify paramters in any order.
```python
def get_initial(name, force_uppercase):
    ...
get_initial(force_uppercase=True, name=first_name)
```
---
>3. I also learn how to call the global variable inside the function.
---
>4. I remember that the third parameter into the loop function FOR means that the steps for each loop. I haven't used this in Python yet.
---
>5. The math operator that elevate a number to the power of the other is represented by the '**'. For example, 10³ can be represented follows, 10 ** 3.
---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
>6. We can use the function round(variable, 2) intead of ':.2f', to reduces the decimal places and rounded them instead of just cutting them.<br>

<br>

<div align="center">

<b>[Back](/web-and-computer-programming/cse-110/README.md)</b>

</div>

<img src="./../../../.github/assets/gradient-bar.svg" width="100%" height="8px"/>
<p align="center">Grow like a 🌳!</p>