# Author: Raphael Carneiro
# Week 4 Project: Word Puzzle

import os
os.system('cls')

print("Welcome to the word 🤔 guessing game!")
# Getting the secret-word by user. It's not a requirement.
secret_word = str(input("\nType your secret word: ")).strip().lower()
# Getting the difficulty by user. It's not a requirement.
difficulty = input("Type the difficulty [HARD] or [EASY]: ").strip().lower()
# Counting the number of letters in the secret word and change them by underscore.
num_letters = len(secret_word)
hidden_word = ['_'] * num_letters
guesses = 0
os.system('cls')

# First try
print("Welcome to the word 🤔 guessing game!\n")
print(f"Your hint is: {' '.join(hidden_word)}")
guess = hidden_word

while guess != secret_word:
    if difficulty == 'hard' and guesses == 5 or difficulty == 'easy' and guesses == 30:
        print(f"Sorry, but the {difficulty} level attempt limit is {guesses}.")
        print(f"It took you {guesses} guesses.")
        break
    else:
        guess = str(input("💭 What is your guess? ")).strip().lower()

        if len(guess) != len(secret_word): # Verifying if the guess length is correct.
            print("Sorry, the guess must have the same number of letters as the secret word.\n")
        elif guess == secret_word:
            guesses += 1
            print("🎉 Congratulations! You guessed it!")
            print(f"It took you {guesses} guesses.")
            break
        else:
            for i in range(num_letters):
                if guess[i] == secret_word[i]:
                    hidden_word[i] = guess[i].upper() # Correct letter and position
                elif guess[i] in secret_word:
                    hidden_word[i] = guess[i].lower() # Correct letter but wrong position 
                else:
                    hidden_word[i] = '_' # Wrong letter
            print(f"Your hint is: {' '.join(hidden_word)}")
        guesses += 1
