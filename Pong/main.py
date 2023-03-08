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
screen.update()
right_handle = Handle('right')
right_handle.set_location(window_width=WINDOW_WIDTH)
screen.update()
ball = Ball()
screen.update()
game_is_on = True
screen.onkey(fun=left_handle.go_up, key='Up')
screen.onkey(fun=left_handle.go_down, key='Down')


def update_score():
    global game_is_on
    if ball.xcor() > WINDOW_WIDTH / 2:
        ball.move_ball_start()
        screen.update()
        score_left.update_score()
        screen.update()
    if ball.xcor() < -1 * (WINDOW_WIDTH / 2) - 100:
        ball.move_ball_start()
        screen.update()
        score_right.update_score()
        screen.update()
    if score_right.score == 5:
        game_is_on = False


def handle_collision_ball():
    if left_handle.head.xcor() - 10 <= ball.xcor() < 0:
        for segment in left_handle.segment_list:
            if ball.distance(segment) < 35:
                ball.dx *= -1
                break
    if 0 < ball.xcor() <= right_handle.head.xcor() + 10:
        for segment in right_handle.segment_list:
            if ball.distance(segment) < 35:
                ball.dx *= -1
                break


while game_is_on:
    right_handle.move_up_and_down(window_height=WINDOW_HEIGHT)
    screen.update()
    left_handle.move(window_height=WINDOW_HEIGHT)
    screen.update()
    update_score()
    handle_collision_ball()
    ball.move(window_height=WINDOW_HEIGHT)
    screen.update()
    time.sleep(0.02)

screen.exitonclick()
