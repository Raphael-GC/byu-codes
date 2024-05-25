#TEAM ACTIVITY

# CORE REQUIREMENT 1
magic_num = int(input('What is the magic number? '))
guess = int(input('What is your guess? '))

if guess < magic_num:
    print('Higher')
elif guess > magic_num:
    print ('Lower')
else:
    print('You guessed it!')


#CORE REQUIREMENT 2
magic_num = int(input('What is the magic number? '))
guess = int(input('What is your guess? '))

while guess != magic_num:
    if guess < magic_num:
        print('Higher')
    elif guess > magic_num:
        print ('Lower')
    guess = int(input('What is your guess? '))

print('You guessed it!')


#CORE REQUIREMENT 3
import random

magic_num = random.randint(1, 100)

guess = int(input('What is your guess? '))

while guess != magic_num:
    if guess < magic_num:
        print('Higher')
    elif guess > magic_num:
        print ('Lower')
    guess = int(input('What is your guess? '))

print('You guessed it!')


#STRETCH CHALLENGE

import random
play_again = 'yes'
while play_again.lower() == 'yes':

    magic_num = random.randint(1, 100)

    num_guesses = 1
    guess = int(input('What is your guess? '))


    while guess != magic_num:
        if guess < magic_num:
            print('Higher')
        elif guess > magic_num:
            print ('Lower')
        guess = int(input('What is your guess? '))
        num_guesses +=1

    print('You guessed it!')
    print(f'You have guessed it {num_guesses} times.')
    play_again = input('Do you want to play again (yes/no)? ')



#STRETCH CHALLENGE BOOLEAN)
import random
play_again = True
yes_no = 'yes'
while play_again == True:

    magic_num = random.randint(1, 100)

    num_guesses = 1
    guess = int(input('What is your guess? '))


    while guess != magic_num:
        if guess < magic_num:
            print('Higher')
        elif guess > magic_num:
            print ('Lower')
        guess = int(input('What is your guess? '))
        num_guesses +=1

    print('You guessed it!')
    print(f'You have guessed it {num_guesses} times.')
    yes_no = input('Do you want to play again (yes/no)? ')
    if yes_no.lower() == 'no':
        play_again = False
        