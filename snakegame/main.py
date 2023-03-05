from turtle import Screen
from snake import Snake
from food import Food

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
play_game = True
screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor('black')
screen.title("Snake Game")
screen.listen()
snake = Snake()
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)
food = Food(WINDOW_WIDTH, WINDOW_HEIGHT)

while play_game:
    snake.move()
    if food.distance(snake.head) < 15:
        food.move_food()
        snake.add_head()
screen.exitonclick()
