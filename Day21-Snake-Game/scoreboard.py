# handle the scoreboard class
from turtle import Turtle
from constants import HEIGHT, WIDTH, PADDING
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


def get_highscore():
    with open("data.txt") as file:
        contents = file.read()
        #print(contents)
    return int(contents)

#print(get_highscore())
    
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # set the initial score to 0, move the turtle to the top of the screen, and write the starting score
        self.score = 0
        self.high_score = get_highscore()
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(x=0, y=HEIGHT // 2 - PADDING * 2)
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # first clear the current scoreboard, then increase the score by 1 and rewrite
        self.score += 1
        self.update_text()

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore()
        self.score = 0
        self.update_text()
    
    def update_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
            



    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
