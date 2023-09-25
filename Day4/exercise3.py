"""
Instructions
You are going to write a program that will mark a spot with an X.

Your job is to write a program that allows you to mark a square on the map using a two-digit system. 

The first digit in the input will specify the column (the position on the horizontal axis).

The second digit in the input will specify the row number (the position on the vertical axis). 
"""
# 🚨 Don't change the code below 👇
row1 = ["O ","O ","O "]
row2 = ["O ","O ","O "]
row3 = ["O ","O ","O "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#row position is the second number in
row_position = int(position[1])
#column position is the first number in
column_position = int(position[0])
#Enter the proper row list first, then the right column element
map[row_position-1][column_position-1] = 'X'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
