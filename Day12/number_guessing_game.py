"""
Checklist for the project:
1. Print a logo at the start of the game
2. Welcome to game message
3. Generate a random number from 1 to 100
3. Choose a difficulty
4. Give 5 guesses for hard and 10 for easy 
5. Let the user enter a guess
6. Tell if the guess was too high or too low
7. Keep looping from step 5 until the user makes the right guess or until
the user runs out of guesses
8. If the user gets the right number, you win message
9. If the user runs out of guesses, you lose message
"""

#import random int function
from random import randint
from art import logo
def game():
    guesses = 0
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number ")
    winning_number = randint(1, 100)
    print(f"winning_number is {winning_number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        guesses = 10
    else:
        guesses = 5
    while guesses > 0:
        print(f"You have {guesses} to get the correct number")
        guess = int(input("Make a guess: "))
        if guess == winning_number:
            print(f"Guessed the number correctly, the number was {winning_number}")
            return
        elif (guess > winning_number):
            print("Too high")
        else:
            print("Too low")
        guesses -= 1
        if guesses == 0:
            print("You've run out of guesses, you lose")
            return

game()
