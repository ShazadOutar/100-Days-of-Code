import time


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(subtract, 2, 3)


# print(result)

# Nested Functions
def outer_function():
    print("Outer")

    def nested_function():
        print("Inner")

    nested_function()


# outer_function()

# Returning a function from a function
def outer_function_with_return():
    print("Outer")

    def nested_function():
        print("Inner")

    return nested_function


# inner_function = outer_function_with_return()
# inner_function()

# Python Decorator Function
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


# the functions with the delay decorator have the added sleep(2)
@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


# functions without the decorator will behave like normal
def say_something():
    print("something")


say_hello()
say_something()
say_bye()
