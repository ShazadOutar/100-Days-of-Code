def my_func(a: int):
    print(a + 2)


my_func(4)

my_num: int
my_num = 2


# specify the type for the inputs and specify the return type
def age_check(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False


if age_check(19):
    print("You can drive")
else:
    print("Please don't drive yet")
