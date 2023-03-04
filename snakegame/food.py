from turtle import Turtle
import random

SIZE = 20
COLOR = 'blue'


class Food():
    def __init__(self, window_width, window_height):
        self.size = SIZE
        self.color = COLOR
        self.window_width = window_width - 20
        self.window_height = window_height - 20
        self.generate_food()

    def generate_food(self):
        random_x = random.randint(0, self.window_width)
        random_y = random.randint(0, self.window_height)
        food = Turtle()
        food.hideturtle()
        food.up()
        food.goto(random_x, random_y)
        food.dot(self.size, self.color)
