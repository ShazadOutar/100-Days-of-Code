# hold all the snake related parts of the code
from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_SEGMENTS = 3
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.block_size = 20
        self.segments = []
        self.create_snake(STARTING_SEGMENTS)
        self.head = self.segments[0]

    def create_snake(self, length):
        # create the snake body
        for i in range(length):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(0 - self.block_size * i, 0)
            self.segments.append(new_segment)

    def move(self):
        # move the snake forward
        # create some variables to make it easier to understand the for loop
        last = len(self.segments) - 1
        first = 0
        step = -1
        # run the loop in reverse order to update the segment to move to the position of the segment ahead of it
        # uses the range of [last, first) so the index 0 isn't being updated by this
        for seg_num in range(last, first, step):
            # get the position of the piece ahead of you and move there
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # seg_num doesn't reach 0 so don't have to worry about reaching index 0 - 1 = -1
            self.segments[seg_num].goto(new_x, new_y)

        # self.segments[first].forward(MOVE_DISTANCE)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # change direction by setting the heading of the first segment
        # to avoid going back on yourself, check if you're not already going opposite your input
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
