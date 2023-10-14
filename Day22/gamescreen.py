"""Create the screen for the game"""
from turtle import Screen
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class GameScreen(Screen):
    def __init__(self):
        super().__init__()
        self.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.exitonclick()


# game = GameScreen()
# my_screen = Screen()
# my_screen.setup()
