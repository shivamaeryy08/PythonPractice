from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 70, 'normal')


class Score(Turtle):
    def __init__(self, location):
        super().__init__()
        self.score = 0
        self.location = location
        self.up()
        self.color('white')
        self.hideturtle()
        self.goto(location)
        self.write(arg=f'{self.score}', align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'{self.score}', align=ALIGNMENT, font=FONT)
