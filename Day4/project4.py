rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

#get the users choice
usr_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

# 0 = Rock, 1 = Paper, 2 = Scissors
options = [rock, paper, scissors]
#if the user input is not a valid option, they instantly lose
if usr_choice > 2 or usr_choice < 0:
    print("You typed an invalid number, you lose")
#continue the game since it's a valid number
else:
    #display the users choice
    print(options[usr_choice])

    #get the computers random choice
    cmp_choice =  random.randint(0, 2)
    print("The computer chose " + options[cmp_choice])

    #I noticed that if with rock being 0, paper being 1, and scissors being 2
    #that the only way the computer would win is if the difference in the two
    #options picked were either 1 or -2 so use that to find when the computer wins
    #and the user wins in every other case
    #or they are equal and its a draw
    choice_diff = cmp_choice - usr_choice
    #if both choose the same option its a draw
    if (usr_choice == cmp_choice):
        print("It's a draw")
    elif (choice_diff == 1) or (choice_diff == -2):
        print("The computer wins!")
    else:
        print("You win!")


