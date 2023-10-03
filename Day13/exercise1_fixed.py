############DEBUGGING#####################


# Describe Problem
# Loops through [1, 20), it might want to print at 20 but 20 will never be reached
#Changing range(1, 20) to range(1, 21) will access i at 20
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")

# my_function()

# Reproduce the Bug
# Using the range of [1, 6] when the range needed is from [0, 5]
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) - 1
# print(dice_imgs[dice_num])

# Play Computer
# There's no output for the input of 1994
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# Indent needed for the print, cast the input to int, and make the print use a fstring
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")

#Print is Your Friend
# double equal signs were used insteal of single for setting the value of word_per_page
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(f"pages is {pages}, words per page is {word_per_page}")
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
#append the new_item to list b each iteration instead of just at the end
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

