from turtle import Turtle

DOWN = 270


class SeparateLine(Turtle):
    def __init__(self, window_height):
        super().__init__()
        self.hideturtle()
        self.up()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0, window_height / 2 - 20)
        end_of_line = (window_height / 2) * -1 + 30
        self.setheading(DOWN)
        while self.ycor() > end_of_line:
            self.down()
            self.forward(20)
            self.up()
            self.forward(20)
