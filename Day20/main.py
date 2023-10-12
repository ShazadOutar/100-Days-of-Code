# from turtle import Turtle, Screen
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# turtle_size = 20
# segments = []
#
# # create the snake body
# for i in range(3):
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(0 - turtle_size * i, 0)
#     segments.append(new_segment)


# move the snake bits
# is_game_on = True
# while is_game_on:
#     # update the screen at the start of the loop
#     screen.update()
#     # delay the snake updating by a certain amount
#     time.sleep(0.5)
#     # create some variables to make it easier to understand the for loop
#     last = len(segments) - 1
#     first = 0
#     step = -1
#     # run the loop in reverse order to update the segment to move to the position of the segment ahead of it
#     # uses the range of [last, first) so the index 0 isn't being updated by this
#     for seg_num in range(last, first, step):
#         # get the position of the piece ahead of you and move there
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         # seg_num doesn't reach 0 so don't have to worry about reaching index 0 - 1 = -1
#         segments[seg_num].goto(new_x, new_y)
#
#     segments[first].forward(20)
#     # segments[first].left(90)

# create the snake using the Snake class from snake.p
game_is_on = True
my_snake = Snake()
# start the event listener
screen.listen()
screen.onkeypress(key="Up", fun=my_snake.up)
screen.onkeypress(key="Down", fun=my_snake.down)
screen.onkeypress(key="Left", fun=my_snake.left)
screen.onkeypress(key="Right", fun=my_snake.right)

while game_is_on:
    screen.update()
    # controls the delay which controls the speed
    time.sleep(0.1)
    my_snake.move()

screen.exitonclick()
