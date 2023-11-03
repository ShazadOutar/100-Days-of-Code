# Improved Phonetic Alphabet Converter
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as error_message:
        # if there is a key-error, print these messages and rerun the function
        print("Please only enter letters")
        print(f"{error_message} is not a letter")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
