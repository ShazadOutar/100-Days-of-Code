from turtle import Turtle
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-SCREEN_WIDTH//2 + 20, SCREEN_HEIGHT//2 - 40)
        self.level = 1
        self.update()

    def increase_level(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=("Ariel", 20, "normal"))

    def game_over(self):
        # self.clear()
        self.goto(0,0)
        self.write("Game Over", move=False, align="center", font=("Ariel", 20, "normal"))
