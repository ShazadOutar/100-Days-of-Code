# draw a square
from turtle import Turtle
from turtle import Screen

my_turtle = Turtle()


def make_square():
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)


make_square()

screen = Screen()
screen.exitonclick()
