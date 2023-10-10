# Make a spirograph (a bunch of circles around one central point)
import turtle
from turtle import Turtle, Screen
import random

# change the color mode to use rgb values from 0, 255
turtle.colormode(255)
t = Turtle()
# increase the speed of the turtle
t.speed("fastest")
# t.speed("fast")


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def spirograph(circles):
    # tilt is how much to rotate after each circle
    tilt = 360 / circles
    current_tilt = 0
    for i in range(circles):
        t.color(get_random_color())
        # each iteration make the circle and then increase the current tilt
        t.circle(100)
        # set the heading by the tilt * the current index
        # ex: i = 2, tilt = 90, setheading(90 + (2 * 90)) = setheading(270)
        t.setheading(tilt + (i * tilt))
        # could also do something with t.setheading = t.heading() + shift_amount


spirograph(100)
screen = Screen()
screen.exitonclick()
