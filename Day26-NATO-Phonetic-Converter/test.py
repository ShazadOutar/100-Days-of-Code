#
#numbers = [1, 2, 3]
#new_list = [n + 1 for n in numbers]
#print(new_list)
#
#"Normal way"
#numbers = [1, 2, 3]
#new_list = []
#for n in numbers:
#	add_1 = n + 1
#new_list.append(add_1)
#
#"list comprehension way"
#numbers = [1, 2, 3]
#new_list = [n + 1 for n in numbers]
#
## modify the output of the range function
#double_range = [n * 2 for n in range(1, 5)]
#
#names = ["Alex", "Beth", "Caroline", "Freddie", "Dave"]
#short_names = [name for name in names if len(name) <= 4]
#
# generate a new dict of random student scores
from random import randint
names = ["Alex", "Beth", "Dave", "Freddie", "Caroline"]
student_scores = {student:randint(0, 100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)
