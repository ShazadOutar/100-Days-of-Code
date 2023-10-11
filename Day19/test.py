# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    # creates a local function in the added function
    def adder(y):
        # adder returns a x + y
        return x + y
    # but create adder returns the function adder
    return adder


add_15 = create_adder(15)

print(add_15(10))


def subtractor(x):
    def minus(y):
        return x - y
    return minus


sub_10 = subtractor(10)
print(sub_10(2))

