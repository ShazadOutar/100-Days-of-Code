"""Main file to handle the snake game"""
from turtle import Screen
from snake import Snake
from constants import HEIGHT, WIDTH, PADDING
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create the snake, food, and scoreboard
game_is_on = True
my_snake = Snake()
new_food = Food()
scoreboard = Scoreboard()
# start the event listener
screen.listen()
screen.onkeypress(key="Up", fun=my_snake.up)
screen.onkeypress(key="Down", fun=my_snake.down)
screen.onkeypress(key="Left", fun=my_snake.left)
screen.onkeypress(key="Right", fun=my_snake.right)
screen.onkeypress(key="q", fun=screen.bye)


while game_is_on:
    # this runs at the start of the loop
    screen.update()
    # controls the delay which controls the speed
    time.sleep(0.1)
    my_snake.move()
    # detect collision with food
    if my_snake.head.distance(new_food) < 15:
        print("Bonk")
        new_food.new_food()
        scoreboard.increase_score()
        my_snake.extend()

    # detect collision with walls
    if (my_snake.head.xcor() > (WIDTH // 2 - PADDING) or my_snake.head.xcor() < (-WIDTH // 2 + PADDING) or
            my_snake.head.ycor() > (HEIGHT // 2 - PADDING)) or my_snake.head.ycor() < (-HEIGHT // 2 + PADDING):
        print("Bonk")
        scoreboard.game_over()
        game_is_on = False

    # detect collision with tail
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
