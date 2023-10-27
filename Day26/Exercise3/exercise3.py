with open("file1.txt") as file1:
    numbers =  file1.readlines()

#print(type(numbers))
#print(numbers)
no_new_line = [num.replace("\n", "") for num in numbers]
no_new_line.pop()
#print(no_new_line)
file1_nums = no_new_line
# print(file1_nums)
def get_nums(file_name):
    with open(file_name) as file:
        numbers = file.readlines()
        removed_new_line = [num.replace("\n", "") for num in numbers]
        removed_new_line.pop()
        file_nums_list = removed_new_line
        file_nums = [int(num) for num in file_nums_list]
        return file_nums

file1_nums = get_nums("file1.txt")
file2_nums = get_nums("file2.txt")
#print(get_nums("file1.txt"))
#print(get_nums("file2.txt"))
print(file1_nums)
print(file2_nums)

result = []
#find which numbers are in both lists
for i in file1_nums:
    if i in file2_nums:
        result.append(i)
for i in file2_nums:
    if i in file1_nums and not in results:
        results.append(i)
print(result)
