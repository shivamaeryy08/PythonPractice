from turtle import Turtle
import random as r
import math


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.dx = r.randint(0, 180)
        self.dy = r.randint(-180, 180)
        self.speed = 0

    def move_ball_start(self):
        self.dx = r.randint(0, 180)
        self.dy = r.randint(-180, 180)
        self.goto(self.dx, self.dy)

    def generate_direction(self, window_height):
        # random_x = r.andint(0, )
        if self.ycor() > window_height / 2 - 100:
            self.dy = -1 * self.dy
        elif self.ycor() < -1 * (window_height / 2) + 100:
            self.dy = -1 * self.dy
        angle = math.degrees(math.atan(self.dy / self.dx))
        print(angle)
        return angle

    def move(self, window_height):
        self.setheading(self.generate_direction(window_height))
        self.speed += 0.1
        self.forward(self.speed)
        # self.setheading(self.generate_direction())
