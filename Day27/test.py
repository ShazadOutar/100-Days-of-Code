def my_add(*args):
    sum = 0
    for n in args:
        print(n)
        sum += n
    return sum

print(my_add(1, 2, 3, 4))
print(my_add(1, 5))
