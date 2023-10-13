# handle the scoreboard class
from turtle import Turtle
from constants import HEIGHT, WIDTH, PADDING
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # set the initial score to 0, move the turtle to the top of the screen, and write the starting score
        self.score = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(x=0, y=HEIGHT // 2 - PADDING * 2)
        self.update_text()

    def update_text(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # first clear the current scoreboard, then increase the score by 1 and rewrite
        self.clear()
        self.score += 1
        self.update_text()

    def game_over(self):
        self.home()
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
