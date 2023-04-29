from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.penup()
        self.hideturtle()

    def generate_car(self):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.goto(300, random.randrange(-230, 270, 20))
        self.all_cars.append(new_car)

    def move_cars(self, difficulty):
        for car in self.all_cars:
            car.penup()
            new_x = car.xcor() - MOVE_INCREMENT * difficulty/2
            car.goto(new_x, car.ycor())
