"""Main file for the Day22 Project"""
from turtle import Screen, Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from paddle import Paddle
print("Pong")

# create the screen for the game
game_screen = Screen()
game_screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
game_screen.bgcolor("black")
game_screen.title("Pong")

game_screen.listen()
paddle = Paddle()
game_screen.onkey(key="w", fun=paddle.up)
game_screen.onkey(key="s", fun=paddle.down)


# keep this last, it doesn't run the code below it
game_screen.exitonclick()
