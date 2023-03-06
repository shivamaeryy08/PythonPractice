from turtle import Screen
from score import Score
from handle import Handle
from separate_line import SeparateLine
from ball import Ball
import time

screen = Screen()
screen.setup(width=1.0, height=1.0)
WINDOW_WIDTH = screen.window_width()
WINDOW_HEIGHT = screen.window_height()
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0, 0)
screen.listen()

score_left = Score((-300, WINDOW_HEIGHT / 2 - 100))
score_right = Score((300, WINDOW_HEIGHT / 2 - 100))
screen.update()
separate_line = SeparateLine(window_height=WINDOW_HEIGHT)
screen.update()
left_handle = Handle('left')
left_handle.set_location(window_width=WINDOW_WIDTH)
right_handle = Handle('right')
right_handle.set_location(window_width=WINDOW_WIDTH)
ball = Ball()
game_is_on = True
screen.onkey(fun=left_handle.go_up, key='w')
screen.onkey(fun=left_handle.go_down, key='s')

while game_is_on:
    right_handle.move_up_and_down(window_height=WINDOW_HEIGHT)
    left_handle.move()
    if ball.xcor() > WINDOW_WIDTH / 2 - 100:
        ball.move_ball_start()
        score_left.update_score()
        screen.update()
    if ball.xcor() < -1 * (WINDOW_WIDTH / 2) - 100:
        ball.move_ball_start()
        score_right.update_score()
        screen.update()
    ball.move(window_height=WINDOW_HEIGHT)
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
