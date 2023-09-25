import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#pick an idex from word_list in the range of [0, length of word list - 1]
#this is how I did it but there's an easier way
#chosen_word = word_list[random.randint(0, len(word_list) - 1)]
#print(chosen_word)
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#iterate through each letter of the word and print if it matched or not
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

