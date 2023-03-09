from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 50, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.score = 0
        self.write(arg=f'Score: {self.score} / 50', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score} / 50', align=ALIGNMENT, font=FONT)
