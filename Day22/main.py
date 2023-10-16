"""Main file for the Day22 Project"""

from turtle import Screen
import time
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BALL_SIZE
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
print("Pong")

# create the screen for the game
game_screen = Screen()
game_screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
game_screen.bgcolor("black")
game_screen.title("Pong")
# remove the animation at the start to draw the paddles
game_screen.tracer(0)

game_screen.listen()
# create the paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# create the ball
ball = Ball((0, 0))

# create the scoreboard
scoreboard = ScoreBoard()

game_screen.onkey(key="Up", fun=left_paddle.up)
game_screen.onkey(key="Down", fun=left_paddle.down)
game_screen.onkey(key="w", fun=right_paddle.up)
game_screen.onkey(key="s", fun=right_paddle.down)
game_screen.onkey(key="q", fun=game_screen.bye)

game_is_on = True
while game_is_on:
    # set the delay
    time.sleep(ball.move_speed)
    game_screen.update()

    # check if it collided with upper or lower boarders
    if ball.ycor() > (SCREEN_HEIGHT // 2 - BALL_SIZE) or ball.ycor() < (-SCREEN_HEIGHT // 2 + BALL_SIZE):
        print("Bonk")
        ball.bounce_y()
        ball.move()
    else:
        # pass
        ball.move()
    # detect collision with paddle
    if (ball.distance(right_paddle) < 30 and ball.xcor() > 320)\
            or (ball.distance(left_paddle) < 30 and ball.xcor() < -320):
        print("blocked")
        ball.bounce_x()

    # detect if the ball went past the right paddle
    if ball.xcor() > 380:
        print("scored")
        # reset the ball position
        ball.ball_reset()
        scoreboard.l_point()
    # past the left paddle
    if ball.xcor() < - 380:
        ball.ball_reset()
        scoreboard.r_point()
# keep this last, it doesn't run the code below it
game_screen.exitonclick()
