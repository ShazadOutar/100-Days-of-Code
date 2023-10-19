# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# names = []
with open("./Input/Names/invited_names.txt") as file:
    names_input = file.readlines()

print(type(names_input[0]))
# remove the \n from each name
names = []
for name in names_input:
    names.append(name.replace("\n", ""))

print(f"New names list {names}")

# get the letter template
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

print(letter)
for name in names:
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w+") as file:
        # file.write(f"Hello {name}")
        temp = letter.replace(f"[name]", f"{name}")
        print(f"new temp is {temp}")
        file.write(temp)
