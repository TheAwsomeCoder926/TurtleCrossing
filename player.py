from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")

    def player_forward(self):
        self.forward(10.0)

    def player_backward(self):
        self.backward(10)

    def change_colour(self, colour):
        self.color(colour)
