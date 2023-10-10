# Trying the idea of the final code
# Use turtle to draw randomized dots in rows on the screen
import random
import turtle
from turtle import Turtle
# can import using an alias
# import turtle as t
# then use my_turtle = t.Turtle
height = 400
width = 400
x_pos = -300
y_pos = -300
turtle.screensize(height, width)
my_turtle = Turtle(shape="turtle")
my_turtle.penup()
my_turtle.setposition(x_pos, y_pos)


def random_rbg_value():
    return random.random()


# my_turtle.dot(20, "Blue")
# my_turtle.forward(100)
print(turtle.colormode())

# for j in range(0, 6):
#     for i in range(0, 6):
#         print(i)
#         r = random_rbg_value()
#         g = random_rbg_value()
#         b = random_rbg_value()
#         my_turtle.pencolor(r, g, b)
#         my_turtle.dot(20)
#         my_turtle.forward(width/6)
#         my_turtle.penup()
#     y_pos += height/6
#     my_turtle.goto(x_pos, y_pos)


def make_box(my_turtle): #, r, g, b):
    # turtle.pencolor(r, g, b)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)


# def rand_color_box(my_turtle):
#     r = random_rbg_value()
#     g = random_rbg_value()
#     b = random_rbg_value()
#     my_turtle.pencolor(r, g, b)
#     my_turtle.pendown()
#     for i in range(4):
#         r = random_rbg_value()
#         g = random_rbg_value()
#         b = random_rbg_value()
#         my_turtle.pencolor(r, g, b)
#         my_turtle.forward(200)
#         my_turtle.left(90)
#
#
# rand_color_box(my_turtle)
# my_turtle.pendown()
# make_box(my_turtle)#, r, g, b)
turtle.exitonclick()
