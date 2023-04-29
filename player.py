from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)

    def move_right(self):
        self.setx(self.xcor() + MOVE_DISTANCE)

    def move_left(self):
        self.setx(self.xcor() - MOVE_DISTANCE)

    def reset_pos(self):
        self.setposition(STARTING_POSITION)
