"""Class for creating and moving the ball"""
from turtle import Turtle
from constants import SCREEN_HEIGHT


class Ball(Turtle):
    def __init__(self, position):
        super().__init__("circle")
        self.color("white")
        # self.penup()
        self.goto(position)
        # use a direction attribute to help with bounce
        self.x_move = 10
        self.y_move = 10

    def move_x(self, distance):
        self.setx(self.xcor() + distance)

    def move_y(self, distance):
        self.sety(self.ycor() + distance)

    def move_angle(self, angle):
        self.setheading(angle)
        self.forward(20)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce_y(self):
        # self.setheading(180)
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def ball_reset(self):
        self.reset()
        self.color("white")
        self.bounce_x()