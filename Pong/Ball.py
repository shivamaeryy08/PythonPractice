from turtle import Turtle
import random as r


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()

    def generate_direction(self):
        pass
        #  if self.xcor() < 0:

    def move(self):
        pass
        # self.setheading(self.generate_direction())
