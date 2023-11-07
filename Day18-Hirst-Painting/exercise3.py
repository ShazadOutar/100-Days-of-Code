# drawing different shapes
from turtle import Turtle, Screen
# import random
from random import random
t = Turtle()


def make_shape(number_of_sides):
    """
    Make a shape based on the number of sides input, each shape made is of a random color
    :param number_of_sides:
    :return:
    """
    # for a square move right by (360/num_sides) degrees
    # a distance of 100/num_sides
    # num_sides times
    degrees = 360 / number_of_sides
    length = 1000/ number_of_sides
    print(f"Degrees: {degrees}")
    r = random()
    g = random()
    b = random()
    # print(f"Length of each side is {length}")
    for _ in range(number_of_sides):
        t.pencolor(r, g, b)
        t.right(degrees)
        t.forward(100)


# make_shape(30)
for i in range(3, 11):
    print(i)
    make_shape(i)

screen = Screen()
screen.exitonclick()
