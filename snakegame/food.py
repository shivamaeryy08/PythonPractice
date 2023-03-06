from turtle import Turtle
import random

SIZE = 1
COLOR = 'blue'


# TODO check if dot needed to be shaped

class Food(Turtle):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.size = SIZE
        self.color = COLOR
        self.window_width = window_width / 2 - 30
        self.window_height = window_height / 2 - 30
        random_x = random.randint(-self.window_width, self.window_width)
        random_y = random.randint(-self.window_height, self.window_height)
        self.shape('circle')
        self.shapesize(stretch_wid=SIZE, stretch_len=SIZE)
        self.fillcolor('blue')
        self.up()
        self.goto(random_x, random_y)

    def move_food(self):
        random_x = random.randint(-self.window_width, self.window_width)
        random_y = random.randint(-self.window_height, self.window_height)
        self.goto(random_x, random_y)
