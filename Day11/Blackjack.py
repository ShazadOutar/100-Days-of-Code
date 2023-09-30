############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

import random
from art import logo

cards = [11, 2, 3, 4]  #, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# create the user and computer hands
user_cards = []
computer_cards = []


#deal card function to be able to give cards
def deal_card(hand, deck):
    """
  Randomly pick a value from the deck to give to the hand picked.
  No return value
  """
    #get a random index from the cards list and then use the value
    random_card = cards[random.randint(0, len(deck) - 1)]
    print(f"The random card is {random_card}")
    #add the random card to the hand
    hand.append(random_card)


def find_sum(hand):
    """
  Checks the current sum of the hand and returns the value
  """
    #noticed I was checking this often to made it a seperate function
    sum = 0
    for card in hand:
        sum += card
    print(f"Sum in has_blackjack is {sum}")
    return sum


def has_blackjack(hand):
    """
  Checks the hand for blackjack. Returns True if found
  """
    sum = find_sum(hand)
    #print(f"Sum in has_blackjack is {sum}")
    if sum == 21:
        print("Blackjack found\n")
        return True
    else:
        return False


def over_21(hand):
    """
  Checks the hand to see if the score is over 21.
  Returns True if over, false otherwise
  """
    sum = find_sum(hand)
    print(f"Sum in over_21 is {sum}")
    if sum > 21:
        print("Over 21")
        return True
    return False


def between_17_and_21():
    """
  Check the computers hand to make sure it's above the minimum of 17 and below the maximum of 21
  """
    sum = find_sum(computer_cards)
    if (sum > 16) and (sum < 21):
        return True
    return False


def give_blackjack(hand):
    hand.append(cards[0])
    hand.append(cards[len(cards) - 1])


def black_jack_game():
    print(logo)
    #deal 2 cards to both players
    for i in range(2):
        deal_card(user_cards, cards)
        deal_card(computer_cards, cards)
    keep_playing = True
    while keep_playing:
        #give_blackjack()
        print(user_cards)
        print(computer_cards)
        #check if the either has blackjack
        #if either does, the game ends
        #the dealer wins if they both have it so dealer gets checked first
        if has_blackjack(computer_cards):
            print("The dealer has blackjack, you lose")
            return
        if has_blackjack(user_cards):
            print("You have blackjack, you win!")
            return
        keep_drawing = input(
            "Enter y to get another card, press n to pass\n").lower()
        #if the player presses y they keep drawing
        if keep_drawing == "y":
            deal_card(user_cards, cards)
        #when the player is done drawing, the computer can draw
        elif keep_drawing == "n":
            #check if the computer has between 16 and 21
            #keep drawing until it's in that range or over
            while not between_17_and_21() or over_21(computer_cards):
                #give the dealer the minimum required score
                deal_card(computer_cards, cards)
                if over_21(computer_cards):
                    print("Computer went over 21, you win")
                    return
                if has_blackjack(computer_cards):
                    print("Computer has blackjack, you lose")
                    return

            if over_21(user_cards):
                print("You went over 21, you lose")
                return
            if over_21(computer_cards):
                print("computer went over 21, you win")
                return

            #at this point the dealer has between 17 and 20 points
            player_score = find_sum(user_cards)
            computer_score = find_sum(computer_cards)
            print(f"Player score is {player_score} and computer score is {computer_score}")
            #compare the two players scores to see who wins
            if player_score > computer_score:
                print("Player has a higher score")
                return
            elif (player_score == computer_score):
                print("It's a draw : ()")
                return
            else:
                print("Computer wins")
                return


      


black_jack_game()
