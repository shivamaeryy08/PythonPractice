from turtle import Turtle
import random

SIZE = 1
COLOR = 'blue'


# TODO check if dot needed to be shaped

class Food(Turtle):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        super().__init__()
        self.size = SIZE
        self.color = COLOR
        self.window_width = WINDOW_WIDTH - 20
        self.window_height = WINDOW_HEIGHT - 20
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
