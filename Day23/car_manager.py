from turtle import Turtle
from random import choice, randint
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    # create the class to make the cars to display
    def __init__(self):
        super().__init__("square")
        self.color(choice(COLORS))
        self.goto(SCREEN_WIDTH // 2 - 20, randint(-200, 200))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.speed_limit = STARTING_MOVE_DISTANCE

    def move(self, level):
        # self.forward(self.speed_limit)
        self.forward(STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT)

    def new_level(self):
        self.speed_limit += 10
