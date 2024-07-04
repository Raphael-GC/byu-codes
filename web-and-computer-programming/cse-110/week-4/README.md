<h1 align="center">
    <img 
        alt="BYU-Idaho"
        title="BYU-Idaho Logo" 
        src="../.github/assets/logo-py.svg" 
        width="60%"
    />

Week 04 - Loops
</h1>
<b>Middle of Week Exercises:</b>

- [While Loops](/web-and-computer-programming/cse-110/week-4/while_loops.py)
- [For Loop](/web-and-computer-programming/cse-110/week-4/for_loop.py)
- [Looping Through Strings](/web-and-computer-programming/cse-110/week-4/looping_through_strings.py)

#### 💡📆 Tip of Week:

> A string is a list of characters, and we can access the position of each character similar to other common lists.
```python
    first_name = "Brigham"
    for letter in first_name:
        print(f"The letter is: {letter}")
```

<b>

[Week's Project: Word Puzzle](/web-and-computer-programming/cse-110/week-4/word_puzzle.py) <br><br>
[Team Activity: Guess My Number](/web-and-computer-programming/cse-110/week-4/team_activity_guess_my_number.py)

#### 💡🤯 What did I learn this week?

>1. Variable `item` in example bellow:
```python
    items = ["crayon", "scissors", "paper", "glitter glue", "markers", "pens"]

    for item in items:
    print(f"The item is: {item}")
```
>What about the variable `item`? Is that a special name? Where does it get defined?

>There is nothing special about the name item in this case. It could have just as easily been called thing or writing_instrument.

>The for loop syntax here is very clever. When you type for item in items:, the list variable, items must already exist, but the variable for each individual element of the list, in this case item, is defined right in that statement. In short, it's saying, "Go through each element of this list and assign a new variable item to be the value each time through.
---
>2. `range()` function for creating a list of items and passing the list of items on the loop.
```python
    # You can create a list for ten numbers this way:
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Or this way.
    numbers = range(10)

    for number in range(10):
    print(number)

    #Output: 
    #0
    #1
    #2
    #3
    #4
    #5
    #6
    #7
    #8
    #9
```
>The `range` function gives you other options like starting at a different number, or counting by 3's, or even going backwards. In all of these cases, the idea of looping through the values is the same. You start with the first one and then continue on, one by one, through the list.

>To start with a different number, you provide two values to the `range` function. If you provide two numbers, it will start with the first one and continue up until (but not including) the second one.

>If you provide three values to the `range` function, it will use the third number as the "step size" or in other words the number to count by.
```python
    # This loop will start with 100, and go up to, but not including 200
    for i in range(100, 200):
        print(i)

    # This loop will do the same thing, but this time, it will count by 10's
    for i in range(100, 200, 10):
        print(i)
```
---
>3. The `len()` function is used to count the number of characters in a string.
```python
    word = "book"
    number_of_letters = len(word) # Notice this can now work for any string

    for index in range(number_of_letters):
        letter = word[index]
        print(f"Index: {index} Letter: {letter}")
```
---
>4. The `enumerate()` function. Using a for loop and the length of the string is a standard way to access both the index and the letter. However, Python also has a way to access both of these variables directly using a special function called enumerate as shown in the following example:
```python
    first_name = "Brigham"

    # Notice by using enumerate, we specify both i and letter
    for i, letter in enumerate(first_name):
        print(f"The letter {letter} is at position {i}")
```

<br>

<div align="center">

<b>[Back](/web-and-computer-programming/cse-110/README.md)</b>

</div>

<img src="./../../../.github/assets/gradient-bar.svg" width="100%" height="8px"/>
<p align="center">Grow like a 🌳!</p>