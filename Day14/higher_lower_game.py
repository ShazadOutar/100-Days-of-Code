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
    print(f"Follower count is {follower_count}")
    return follower_count 




def game():
    """
    The main game function to organize the steps and subfunctions together
    """
    # print the logo
    print(art.logo)
    # access a random element of the data dictonary
    # print(data[1])
    # store the size of the number of elements in data
    size_of_data = len(data)
    # print(size_of_data)
    # the last index is the size - 1
    
    # Idea 1 
    #person_a = randint(0, size_of_data - 1)
    # print(data[49])
    #person_b = randint(0, size_of_data - 1)
    #show_person(person_a)
    #show_person(person_b)
    #person_a_followers = get_follower_count(person_a)

    # Idea 2
    # Get the persons data from a random index in the list
    person_a = data[randint(0, size_of_data - 1)]
    print(person_a)
    person_b = data[randint(0, size_of_data - 1)]
    print(person_b)
    
    #show each person to help with debugging
    show_person(person_a)
    show_person(person_b)

    # Get each persons follower count
    person_a_followers = get_follower_count(person_a)
    print(person_a_followers)
    person_b_followers = get_follower_count(person_b)
    print(person_b_followers)

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
    guess = input("Who has more followers? Type 'A' or 'B'").lower()
    
    # Check if the user guessed correctly or not


    return


game()
