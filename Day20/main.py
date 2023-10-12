import turtle
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

turtle_size = 20
segments = []

# create the snake body
for i in range(3):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(0 - turtle_size * i, 0)
    segments.append(new_segment)


def turn_left(turtle_num):
    turtle_num.left(90)


# move the snake bits
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(1)
    last = len(segments) - 1
    first = 0
    step = -1
    for seg_num in range(last, first, step):
        print(seg_num)

screen.exitonclick()
