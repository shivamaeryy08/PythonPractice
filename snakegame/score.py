from turtle import Turtle


class Score(Turtle):
    def __init__(self, WINDOW_HEIGHT):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.setposition(0, WINDOW_HEIGHT - 30)
        self.write(arg=f'Score: {self.score}', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', font=('Arial', 20, 'normal'))

    def display_loss(self):
        self.clear()
        self.write(arg=f'You Lose! Total Score: {self.score}', font=('Arial', 20, 'normal'))
