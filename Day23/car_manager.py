from turtle import Turtle
from random import choice, randint
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    # create the class to make the cars to display
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        # super().__init__("square")
        # self.color(choice(COLORS))
        # self.goto(SCREEN_WIDTH // 2 - 20, randint(-200, 200))
        # self.shapesize(stretch_wid=1, stretch_len=2)
        # self.setheading(180)
        # self.speed_limit = STARTING_MOVE_DISTANCE

    def create_cars(self):
        # use random chance to limit how often the cars are made
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    # def move(self, level):
    #     # self.forward(self.speed_limit)
    #     self.forward(STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def new_level(self):
        self.car_speed += MOVE_INCREMENT

