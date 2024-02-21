# Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    # Use positional arguments with *args to get the input needed for create_blog_post
    def wrapper(*args, **kwargs):
        print(args[0])  # this is the first argument, so for create_blog_post, that's the user
        # args[0] == user object
        if args[0].is_logged_in == True:
            function(args[0])

    return wrapper


# This function should only print when the input user has is_logged_in set to True
@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


person_1 = User("Steve")
# Create blog post won't run now because of the decorator and is_logged_in starting at False
create_blog_post(person_1)
person_1.is_logged_in = True
create_blog_post(person_1)


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.fuel = 0


def fuel_check_decorator(function):
    def wrapper_function(*args):
        # args[0] for the drive function is the input car object
        if args[0].fuel <= 0:
            print("Out of fuel ⛽")
        else:
            function(args[0])

    return wrapper_function


def show_brand_decorator(function):
    def wrapper_function(*args):
        print(args[0].brand)
        function(args[0])

    return wrapper_function


# It seems like the order of the decorators matters and if the function being wrapped runs or not
@show_brand_decorator
@fuel_check_decorator
def drive(car):
    # drive the car but only when there is more than 0 gas in the tank
    print("Vroom!")


car_1 = Car("Nissan")
drive(car_1)
car_1.fuel = 100
drive(car_1)
