from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

play_game = True
screen = Screen()
screen.setup(width=1.0, height=1.0)
WINDOW_WIDTH = screen.window_width()
WINDOW_HEIGHT = screen.window_height()
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0, 0)
screen.listen()
snake = Snake()
screen.update()
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)
food = Food(WINDOW_WIDTH=WINDOW_WIDTH, WINDOW_HEIGHT=WINDOW_HEIGHT)
screen.update()
score = Score(WINDOW_HEIGHT=WINDOW_HEIGHT)
screen.update()
distance_boundary = 20
while play_game:
    out_bounds = snake.head.xcor() > WINDOW_WIDTH / 2 - distance_boundary or snake.head.xcor() < (
            -1 * (
            WINDOW_WIDTH / 2 - distance_boundary)) or snake.head.ycor() > WINDOW_HEIGHT / 2 - distance_boundary or snake.head.ycor() < (
                         -1 * (WINDOW_HEIGHT / 2 - distance_boundary))
    if snake.detect_collision() or out_bounds:
        play_game = False
        score.display_loss()
        screen.update()
    else:
        time.sleep(0.03)
        snake.move()
        screen.update()
        if food.distance(snake.head) < 17:
            food.move_food()
            snake.add_head()
            score.update_score()
            screen.update()
screen.exitonclick()
