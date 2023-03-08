from turtle import Turtle
import random as r
import math


def generate_random_angle():
    while True:
        x = r.uniform(-1 * (math.sqrt(3) / 2), (math.sqrt(3) / 2))
        if x == 0.0:
            continue
        y = r.uniform(-1 * (math.sqrt(3) / 2), (math.sqrt(3) / 2))
        angle = math.degrees(math.atan2(y, x))
        invalid_pos_angle = 80 <= angle <= 100 or 250 <= angle <= 290 or angle == 0
        invalid_neg_angle = -80 <= angle <= -100 or -250 <= angle <= -290 or angle == 0
        if not (invalid_neg_angle or invalid_pos_angle):
            return x, y


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.dx = generate_random_angle()[0]
        self.dy = generate_random_angle()[1]
        self.speed = 15

    def move_ball_start(self):
        self.dx = generate_random_angle()[0]
        self.dy = generate_random_angle()[1]
        self.goto(self.dx, self.dy)
        self.speed = 15

    def move(self, window_height):
        # random_x = r.andint(0, )
        if self.ycor() > window_height / 2 - 60:
            self.dy = -1 * self.dy
        elif self.ycor() < -1 * (window_height / 2) + 100:
            self.dy = -1 * self.dy
        angle = math.degrees(math.atan2(self.dy, self.dx))
        self.setheading(angle)
        self.speed += 0.05
        self.forward(self.speed)
        # self.setheading(self.generate_direction())
