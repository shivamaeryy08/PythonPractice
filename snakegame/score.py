from turtle import Turtle


class Score(Turtle):
    def __init__(self, WINDOW_HEIGHT):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.write(f'Score: {self.score}')
        self.setposition(0, WINDOW_HEIGHT - 30)
        self.hideturtle()
