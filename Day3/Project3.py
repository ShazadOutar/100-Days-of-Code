"""
Instructions
Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.

To write your code according to my story, you can use this flow chart from draw.io to help you.

However, I think the fun part is writing your own story 😊
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
#Decision #1
choice_1 = input("There are 2 roads you can take, go left or go right.\nPick your path by entering left or right. ").lower()
if choice_1 == "left":
    print("The ground breaks under you.\nGame Over.")
elif choice_1 == "right":
    #get the input for the second decision
    #decision #2
    choice_2 = input("You find a house, do you enter from the front door or the back door.\nPick either front or back. ").lower()
    if choice_2 == "front":
        print("You've been caught\nGame Over")
    elif choice_2 == "back":
        print("You've entered a strange house")
        #decision #3
        choice_3 = input("Do you look for the treasure in the basement, the kitchen, or the backyard ").lower()
        if choice_3 == "backyard":
            print("You've been caught\nGame Over")
        elif choice_3 == "kitchen":
            print("You've been caught\nGame Over")
        elif choice_3 == "basement":
            print("You've found the treasure!")
        else:
            print("Game Over")

    else:
        print("Game Over")

else:
    print("Game Over")
