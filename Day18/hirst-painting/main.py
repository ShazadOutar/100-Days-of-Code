# import colorgram
#
# # colors is a list of rgb values
# colors = colorgram.extract("painting.jpg", 20)
# # print(colors[0])
# # first_color = colors[0]
# # rgb = first_color.rgb
# # print(rgb)
# # print(rgb[0])
# # print(rgb.r)
#
# rgb_colors = []
# for color in colors:
#     # print(color.rgb)
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
# use the previous code to get the color list from the painting image
# import turtle
import turtle

color_list = [
    (194, 214, 239), (58, 105, 125), (135, 165, 190), (14, 35, 50), (141, 83, 50), (64, 25, 12),
    (196, 150, 109), (236, 233, 230), (162, 190, 228), (32, 165, 186), (7, 88, 107), (119, 44, 19),
    (32, 21, 26), (237, 251, 251), (181, 126, 63), (112, 127, 147), (9, 16, 14), (101, 88, 93),
    (124, 218, 239), (159, 151, 155)
]
# Using this color list make a 10x10 rows of spots of colors from this color list
# The spots should be 20 in size and 50 apart
from turtle import Turtle, Screen
from random import choice

my_turtle = Turtle()
turtle.colormode(255)


def get_color():
    """
    Get a random color from color choice list
    :return:
    """
    return choice(color_list)


def make_painting():
    # make the first row
    for j in range(10):
        for i in range(10):
            my_turtle.dot(20, get_color())
            my_turtle.penup()
            my_turtle.forward(50)
        my_turtle.penup()
        my_turtle.sety(my_turtle.ycor() + 50)
        my_turtle.setx(-200)


# set the turtle close to the bottom left
my_turtle.penup()
my_turtle.setposition(-200, -200)
# print(my_turtle.ycor())
make_painting()
my_turtle.hideturtle()
screen = Screen()
screen.exitonclick()
