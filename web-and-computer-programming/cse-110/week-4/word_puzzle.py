# Author: Raphael Carneiro
# Week 4 Project: Word Puzzle

print("Welcome to the word guessing game!")
secret_word = "Abinadi"
guesses = 1
guess = str(input("What is your guess? "))

while guess.lower() != secret_word.lower():
    print("Your guess was not correct.")
    guesses += 1 
    guess = str(input("What is your guess? "))

print("Congratulations! You guessed it!")
print(f"It took you {guesses} guesses.")