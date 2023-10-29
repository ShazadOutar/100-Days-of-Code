# how to iterate over a pandas dataframe
student_dict = {
    "student": ["John", "James", "David"],
    "score": [56, 34, 90]
}
# to loop through a dictionary
# for (key, value) in student_dict.items():
#    print(key)
#    print(value)

import pandas 

# can iterate the same as in a dict
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for (key, value) in student_data_frame.items():
    # print(key)
    # print(value)


# Or can use the inbuilt iterator
# loop through rows of a dataframe
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "David":
        print(row.score)
