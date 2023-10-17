# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# use this to avoid having to use file.close
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# write to a file
with open("my_file.txt", mode="w") as file:
    file.write("New text")
