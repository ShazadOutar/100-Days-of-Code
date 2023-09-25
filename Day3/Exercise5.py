"""
# Love Calculator Assignment
# Find a love score between two people by:
# Take both names and check the number of times
# the letters in the word TRUE occurs
# Then check for the number of times
# the letters in the word LOVE occurs in both names
# Then combine these numbers to make a 2 digit number
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
#combine both names into one string, all lowercase
both_names = name1.lower() + name2.lower()

#count and store the amount of each letter
count_t = both_names.count("t")
count_r = both_names.count("r")
count_u = both_names.count("u")
count_e = both_names.count("e")
digit_1 = count_t + count_r + count_u + count_e

count_l = both_names.count("l")
count_o = both_names.count("o")
count_v = both_names.count("v")
count_e = both_names.count("e")
digit_2 = count_l + count_o + count_v + count_e

#make the digits into strings to combine them
score_str = str(digit_1) + str(digit_2)
#then cast to an integer to compare the score ranges
score_int = int(score_str)

if score_int < 10 or score_int > 90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int > 40 and score_int < 50:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}.")


