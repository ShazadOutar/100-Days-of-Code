"""
Problem Breakdown:
1. Create a player turtle and move forward when the user presses up
2. Create cars to move across the screen, from right to left
2a. The cars are of the same speed and are random colors
3. If the turtle reaches the top, it resets and a new level starts. Same as before but increased car speed
4. When there a car hits the turtle, game over and everything freezes
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from constants import SCREEN_HEIGHT

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# create the player turtle
player = Player()

# create the car manager
car_manager = CarManager()

# create the scoreboard
scoreboard = Scoreboard()

screen.onkey(fun=player.move, key="Up")
screen.onkey(fun=screen.bye, key="q")

game_is_on = True
cars = []
# count = 0
# level = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # check for collisions
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # if count % 6 == 0:
    #     print(f"Count is {count}")
    #     new_car_manager = CarManager()
    #     cars.append(new_car_manager)
    #
    # for car in cars:
    #     car.move(level)
    #
    #     # check for collisions
    #     # if (abs(player.ycor() - car.ycor()) < 10) and (abs(player.xcor() - car.xcor()) < 20):
    #     if player.distance(car) < 20:
    #         print(f"Player ycor is {player.ycor()} and car ycor is {car.ycor()}")
    #         print(f"Player xcor is {player.xcor()} and car xcor is {car.xcor()}")
    #         print("Bonk")
    #         scoreboard.game_over()
    #         # game_is_on = False

    # check for when the player reaches the finish line
    # if player.ycor() > SCREEN_HEIGHT // 2 - 50:
    #     print("Level completed")
    #     player.new_level()
    #     level += 1
    #     scoreboard.update(level)
    if player.is_at_finish_line():
        player.new_level()
        car_manager.new_level()
        scoreboard.increase_level()

    # count += 1

screen.exitonclick()