student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
#scores and grades are both already dicts
for key in student_scores:
    #could've also used score = student_scores[key]
    #failed if below 70
    if student_scores[key] <=70:
        student_grades[key] = "Fail"
    #if above 70 and below 80
    elif student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    #if above 80 and below 90
    elif student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    #if above 90 and below 100
    elif student_scores[key] <= 100:
        student_grades[key] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)
