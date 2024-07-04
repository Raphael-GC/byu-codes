# Write a program that asks the user for their favorite letter.
# Then, loop through a programmed word one letter at a time.
# If the letter in the programmed word is the user's favorite,
# you'll first print it out as a capital letter, then later you will "hide" it.
# If the letter is not their favorite you will print it out as a lower case letter.

# CHALLENGE #1
word = "Commitment"

"""
for letter in word:
    if letter == 'm':
        print(letter.upper())
    else:
        print(letter.lower())

print()
"""

# CHALLENGE #2
"""
favorite_letter = input("Enter your favorite letter: ").lower()

for i in range(len(word)):
    if word[i] == favorite_letter.lower():
        word = list(word) # Turn the string into a list.
        word.pop(i)
        word.insert(i, favorite_letter.upper())
        word = ''.join(word) # Make the characters be gathered.

print(word)
"""

# CHALLENGE #3
favorite_letter = input("Enter your favorite letter: ").lower()
for i in range(len(word)):
    if word[i] == favorite_letter.lower():
        word = list(word) # Turn the string into a list.
        word.pop(i)
        word.insert(i, "_")
        word = ''.join(word) # Make the characters be gathered.

print(word)
