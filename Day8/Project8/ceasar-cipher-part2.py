alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift_amount, direction):
    #same as before, make a new string to hold the final message
    new_text = ""
    #loop to get each letter position in the alphabet for encoding/decoding
    for letter in text:
        position = alphabet.index(letter)
        #add of subtract is the only difference between encoding and decoding
        if direction == "encode":
            new_position = (position + shift_amount) % len(alphabet)
        elif direction == "decode":
            new_position = (position - shift_amount) % len(alphabet)
        new_text += alphabet[new_position]
    print(f"The {direction}d text is {new_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text, shift_amount=shift, direction=direction)
