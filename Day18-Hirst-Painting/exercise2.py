# draw a dashed line

from turtle import Turtle


my_turtle = Turtle()
for i in range(15):
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
