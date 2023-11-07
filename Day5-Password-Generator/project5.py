"""
The program will ask:

How many letters would you like in your password?

How many symbols would you like?

How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.
"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#create an empty list to hold the random letters to use
random_letters = []
#print(random_letters)

#loop the number of times that the user picked for the number of letters
for num in range(1, nr_letters + 1):
    #generate a random int in the range of [0, last index of letters]
    random_letter = random.randint(0, len(letters) - 1)
    #print(f"Random number is: {random_letter}")
    #print("Random letter is: " + letters[random_letter])
    #use the random letter index to pick a letter to append to the random letters list
    random_letters.append(letters[random_letter])
#print(random_letters)

#create an empty list to hold the random numbers to use
random_numbers = []

#loop through the number of numbers to use
for num in range(1, nr_numbers + 1):
    #generate a random int in the range of [0, last index of numbers]
    random_number = random.randint(0, len(numbers) - 1)
    #use the randomly picked number to be the index of the number to use and add it to the list of random_numbers
    random_numbers.append(numbers[random_number])
#print(random_numbers)

#same process as above for generating the random symbols list

#create an empty list to hold the random symbols to use
random_symbols = []

#loop through the number of symbols to use
for num in range(1, nr_symbols + 1):
    #generate a random int in the range of [0, last index of symbols]
    random_symbol = random.randint(0, len(symbols) - 1)
    #use the randomly picked number to be the index of the number to use and add it to the list of random_symbols
    random_symbols.append(symbols[random_symbol])
#print(random_symbols)

#using the random_letters list as base list, insert the other two lists into it
password = random_letters
#print(f"Password is currently: {password}")

#loop through all of the random_numbers list
for num in random_numbers:
    #the insert function is in the form list.insert(i, x)
    #with i being the position/index to insert into
    #and x being the value to insert
    #so I broke it up into 2 small variables to use first and then combine
    #pick a random index to insert the values of the random_numbers list
    index = random.randint(0, len(random_letters) - 1)
    value = num
    password.insert(index, value)
#print(f"Password is currently: {password}")

#similar process but use the symbols list now with the new random password string
for symbol in random_symbols:
    index = random.randint(0, len(random_symbols) - 1)
    value = symbol
    password.insert(index, value)
#print(password)

#Finally join all the list elements into one string
password_str = ""
for letter in password:
    password_str += letter
print('Your password is ' + '"' + password_str + '"')


