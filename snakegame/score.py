from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Score(Turtle):
    def __init__(self, WINDOW_HEIGHT):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.setposition(0, WINDOW_HEIGHT / 2 - 30)
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def display_loss(self):
        self.clear()
        self.write(arg=f'You Lose! Total Score: {self.score}', align=ALIGNMENT, font=FONT)
