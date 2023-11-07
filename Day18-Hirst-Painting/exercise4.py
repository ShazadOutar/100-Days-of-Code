# Generate a random walk using the turtle and speed it up
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
t = Turtle()
# make the lines thicker
t.pensize(10)
# max out the drawing speed
t.pen(speed=0)


def set_random_color():
    # set turtle to a random color
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor(r, g, b)

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_move():
    # pick a random direction and move forward by 50
    # set_random_color()
    t.pencolor(get_random_color())
    # randrange is inclusive so use the range [0, 270] or [90, 360]
    turn_amount = random.randrange(0, 270, 90)
    t.right(turn_amount)
    t.forward(50)


for _ in range(100):
    print(_)
    random_move()

screen = Screen()
screen.exitonclick()
