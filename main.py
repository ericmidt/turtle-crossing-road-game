import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_is_on = True
counter = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if counter == 5:
        car_manager.generate_car()
        counter = 0
    car_manager.move_cars(score.score)
    
    # Detects if player reached the other side of the road
    if player.ycor() > 280:
        score.increment_score()
        player.reset_pos()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            score.game_over()

    counter += 1

screen.exitonclick()
