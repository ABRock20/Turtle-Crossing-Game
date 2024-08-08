import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# Create a turtle player that starts at the bottom of the screen
player = Player()

# creating the car
car_manager = CarManager()

# creating the scorecard
scoreboard = Scoreboard()

#  listen for the "Up" keypress to move the turtle north
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # car creation and movement
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect turtle finished the top edge
    if player.finish():
        player.refresh()
        scoreboard.score_point()
        car_manager.speed_up()


screen.exitonclick()
