# Author: Raphael Carneiro
# Week 3 Project: Adventure Game
import os
# Introduction
input("If you'd like to progress through the story, simply press [ ENTER⬇️ ] after each sentence to reveal the next.")
input("The only exception would be if there is a question, in which case you should type your response and press [ ENTER⬇️ ].")
input("✨ Welcome to the world of Pokémon! My name is Rapha!👨🏾‍💼")
input("People call me the Pokémon Professor!")
input("🌎This world is inhabited by creatures called Pokémon!🦖")
input("Today, you will have to complete 5 missions or battles.💥")

# Cleaning the screen
os.system('clear') or None

# First question
starter_type = str(input("Choose which Pokémon type will be your starter, typing 🌱GRASS or 🔥FIRE or 🌊WATER: "))
input(f"You choose the type {starter_type.title()}.")
