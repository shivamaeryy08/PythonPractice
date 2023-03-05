from turtle import Turtle
import random

SIZE = 1
COLOR = 'blue'


class Food(Turtle):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.size = SIZE
        self.color = COLOR
        self.window_width = window_width - 20
        self.window_height = window_height - 20
        random_x = random.randint(-self.window_width, self.window_width)
        random_y = random.randint(-self.window_height, self.window_height)
        self.shape('circle')
        self.hideturtle()
        self.shapesize(stretch_wid=SIZE, stretch_len=SIZE)
        self.fillcolor('blue')
        self.speed('fastest')
        self.up()
        self.goto(random_x, random_y)
        self.showturtle()

    def move_food(self):
        random_x = random.randint(-self.window_width, self.window_width)
        random_y = random.randint(-self.window_height, self.window_height)
        self.goto(random_x, random_y)
