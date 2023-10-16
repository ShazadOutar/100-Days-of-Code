"""Paddle Class"""
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        # create the paddle and position it
        super().__init__("square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)

    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)
