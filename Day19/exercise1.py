# make an etch-a-sketch app
# w for forwards, s for backwards
# a for counter-clockwise, d for clockwise
# c to clear the drawing
import turtle
from turtle import Turtle, Screen

# def get_user_option():
#     return input("Direction\n").lower()
#     return "space"
distance = 20
degrees = 10


def move_forward():
    my_turtle.forward(distance)


def move_backwards():
    my_turtle.forward(-distance)


def rotate_clockwise():
    # print(my_turtle.heading())
    # increase the heading by 90
    my_turtle.setheading(my_turtle.heading() - degrees)


def rotate_counter_clockwise():
    my_turtle.setheading(my_turtle.heading() + degrees)


def clear_drawing():
    my_turtle.reset()


# print(get_user_option())
my_turtle = Turtle()
screen = Screen()


def quit():
    screen.bye()


# def dir_move():
#     # no parameters for the whole function
#     def move_forward(distance):
#         my_turtle.forward(distance)
#     return move_forward
#
# # call dir_move() and then set the value of move_forward by
# move_turt = dir_move()
# move_turt(100)

# start the screen event listener
screen.listen()
# listen for the keys we want
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="q", fun=quit)
screen.exitonclick()
