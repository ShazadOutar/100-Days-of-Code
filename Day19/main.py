# turtle race
from turtle import Turtle, Screen
import random

screen = Screen()
width = 500
height = 400
padding = 40
race_spacing = 50
is_race_on = False
starting_line = -width / 2 + padding
finish_line_x = width / 2 - padding

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen.setup(width=width, height=height)
user_guess = screen.textinput(title="Make your bet", prompt="Which color do you think will win? Enter a color")

# draw finish line
finsh = Turtle()
finsh.hideturtle()
finsh.penup()
finsh.goto(finish_line_x + 20, -height / 2 + padding)
finsh.left(90)
finsh.pendown()
finsh.forward(height - padding * 2)

racers = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(starting_line, -height / 2 + padding * (turtle_index + 1))
    racers.append(new_turtle)

# manually setting all the values of the turtles
# # make and set red turtle
# turtle_1 = Turtle(shape="turtle")
# turtle_1.color(colors[0])
# turtle_1.penup()
# turtle_1.goto(starting_line, -height / 2 + padding)

# wait until the user enters a guess before the race starts
if user_guess:
    is_race_on = True

winning_turtle = ""

while is_race_on:
    for turtle_index in racers:
        if turtle_index.xcor() > finish_line_x:
            is_race_on = False
            winning_turtle = turtle_index.pencolor()
            if winning_turtle == user_guess:
                print(f"You've won! The winning color is {winning_turtle}")
            else:
                print(f"You've lost. The winning color is {winning_turtle}")
        random_distance = random.randint(1, 10)
        turtle_index.forward(random_distance)

print(winning_turtle)
screen.exitonclick()
