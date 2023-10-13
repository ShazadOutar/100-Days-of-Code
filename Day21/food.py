from turtle import Turtle
from random import randint
from constants import WIDTH, HEIGHT, PADDING


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        # use randint with range of half the width and some padding
        rand_x = randint(-(WIDTH // 2) + PADDING, WIDTH // 2 - PADDING)
        rand_y = randint(-(HEIGHT // 2) + PADDING, HEIGHT // 2 - PADDING)
        self.goto(rand_x, rand_y)
