import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
letter_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter: row.code for (index, row) in letter_data_frame.iterrows()}
# print(letter_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_word = input("Enter a word: ").upper()
# for i in user_word:
#     # get each value for the letter key
#     print(letter_dict[i])
word = input("Enter a word: ").upper()
result = [letter_dict[letter] for letter in word]
print(result)
