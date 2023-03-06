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
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
food = Food(window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT)
screen.update()
score = Score(window_height=WINDOW_HEIGHT)
screen.update()
distance_boundary = 20
while play_game:
    if snake.detect_collision(window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                              distance_boundary=distance_boundary):
        play_game = False
        score.display_loss()
        screen.update()
    else:
        time.sleep(0.02)
        snake.move()
        screen.update()
        if food.distance(snake.head) < 17:
            food.move_food()
            snake.add_head()
            score.update_score()
            screen.update()
screen.exitonclick()
