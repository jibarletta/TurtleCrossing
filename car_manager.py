from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """Creates the cars."""
    def __init__(self):
        super().__init__()
        self.autos = []
        # self.create_car()
        increment = 0

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        self.autos.append(new_car)
# TODO: ACA ARME LISTA PARA CADA AUTO, HAY QUE DARLES LA ORDEN DE MOVERSE
    def move(self):
        self.goto(x=280, y=random.randint(-280, 280))
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        # self.goto(x=new_x + increment, y=self.ycor())
        self.backward(STARTING_MOVE_DISTANCE)


    def lvl_up(self):
        pass
