sentence = input()
#sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#print(sentence)

# turn the input into a dictionary of (word, word_length)
result = {word:len(word) for word in sentence.split(" ")}
print(result)
