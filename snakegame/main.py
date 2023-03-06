from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
play_game = True
screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
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

while play_game:
    if snake.detect_collision():
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
