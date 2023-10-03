"""
The game is to compare 2 people by the amount of followers they have.
Steps:
1. Print the logo
2. Show person A and their info
3. Print vs logo
4. Show person B and their info
5. Let the user guess who has more followers
6a. If the user is wrong, end the game and print their score
6b. If the guess is right, increase the score by 1 and loop back from step 1
"""

import art 
from game_data import data
from random import randint

#def show_person(person_index):
#    """
#    Get the persons index and prints their info from the data dictionary
#    """
#    print(person_index)
#    print(data[person_index])
#    person = data[person_index]
#    name = person.get("name")
#    followers = person.get("follower_count")
#    print(f"Person at {person_index} is: {name}, with {followers} followers.")
#    #print(data[person_index].get("name"))
#

def show_person(person):
    name = person.get("name")
    followers = person.get("follower_count")
    print(f"Person is: {name}, with {followers} followers.")


def get_follower_count(person):
    """
    Input the person and return the follower count of the person
    """
    #print(f"person is: {person}")
    follower_count = person.get("follower_count")
    #print(f"Follower count is {follower_count}")
    return follower_count 




def game(person_a, score):
    """
    The main game function to organize the steps and subfunctions together
    """
    #set the starting score to 0
    #score = 0
    #print(f"score at the start of loop is {score}")
    correct = True
    # Start the loop
    # print the logo
    print(art.logo)
    # access a random element of the data dictonary
    # print(data[1])
    # store the size of the number of elements in data
    size_of_data = len(data)
    # print(size_of_data)
    # the last index is the size - 1
    
    # Idea 2
    # Get the persons data from a random index in the list
    #person_a = data[randint(0, size_of_data - 1)]
    #print(person_a)
    person_b = data[randint(0, size_of_data - 1)]
    #print(person_b)
    
    # show each person to help with debugging
    show_person(person_a)
    print(art.vs)
    show_person(person_b)

    # Get each persons follower count
    person_a_followers = get_follower_count(person_a)
    #print(person_a_followers)
    person_b_followers = get_follower_count(person_b)
    #print(person_b_followers)

    # Get the user with the highest follower count
    # Use the highest var to check the users input
    highest = ""
    if person_a_followers > person_b_followers:
        print("Person a has more followers")
        highest = "a"
    else:
        print("Person b has more followers")
        highest = "b"

    # Get the users guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Check if the user guessed correctly or not
    #print(f"highest is {highest}")
    if guess == highest:
        #print("User guessed correctly")
        correct = True
        score += 1
        print(f"Your right! Current score is {score}")
        # person b is the new person a
        return(game(person_b, score))
    else:
        correct = False
        print("Game over")
        return score

    print(f"Ending score is {score}")
    return score


person_a = data[randint(0, len(data) - 1)]
score = 0
# Pass the person a as a parameter to be able reuse the same person as the new person a
print(f"Final score is {game(person_a, score)}")

