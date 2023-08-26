from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.colour_list = ["red", "yellow", "indigo", "khaki", "chocolate", "olive", "blue", "gold"]

    def new_car(self):
        y_cord = random.randint(-280, 280)
        colour_choice = random.choice(self.colour_list)
        car = Turtle()
        car.shape("square")
        car.color(colour_choice)
        car.shapesize(stretch_wid=3, stretch_len=1)
        car.goto(x=320, y=y_cord)
