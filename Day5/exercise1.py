#You are going to write a program that calculates the average student height from a List of heights.
#Don't use len() or sum(), only for loop

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#hold the sum and a count as we loop through
height_sum = 0
count = 0

#loop the list
for student in student_heights:
    #increase the sum of the heights by the current student
    height_sum += student
    #increase the 
    count += 1
average = int(round(height_sum / count, 0))
print(average)
