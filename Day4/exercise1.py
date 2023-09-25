"""
Generate a 0 or 1 to be either heads or tails
"""
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random

flip = random.randint(0, 1)
if flip == 1:
    print("Heads")
if flip == 0:
    print("Tails")
