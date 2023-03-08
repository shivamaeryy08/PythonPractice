from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Score(Turtle):
    def __init__(self, window_height):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color('white')
        self.setposition(0, window_height / 2 - 30)
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        with open('./high-score.txt', mode='r') as file:
            prev_high_score = file.read()
        self.write(arg=f'Score: {self.score}  High Score: {prev_high_score}', align=ALIGNMENT, font=FONT)

    def display_loss(self):
        self.clear()
        self.write(arg=f'You Lose! Total Score: {self.score}', align=ALIGNMENT,
                   font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
            with open('./high-score.txt', mode='w') as file:
                file.write(f"{self.high_score}")
