from turtle import Turtle

square = Turtle('square')
square.color('white')
square.speed("slowest")
square.penup()
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.score = 0
        self.square_list = [square]
        self.head = square
        self.tail = square

    def move(self):
        for i in range(len(self.square_list) - 1, 0, 1):
            cur_square = self.square_list[i]
            pos_mov_to = self.square_list[i - 1].position()
            cur_square.goto(pos_mov_to)
        self.head.forward(DISTANCE)

    def turn_right(self):
        self.head.setheading(RIGHT)

    def turn_left(self):
        self.head.setheading(LEFT)

    def turn_down(self):
        self.head.setheading(DOWN)

    def turn_up(self):
        self.head.setheading(UP)

    def add_head(self):
        prev_head = self.head
        new_head = Turtle('square')
        new_head.color('white')
        new_head.penup()
        if prev_head.heading() == UP:
            new_head.goto(prev_head.xcor(), prev_head.ycor() + 20)
        elif prev_head.heading() == DOWN:
            new_head.goto(prev_head.xcor(), prev_head.ycor() - 20)
        elif prev_head.heading() == LEFT:
            new_head.goto(prev_head.xcor() - 20, prev_head.ycor())
        else:
            new_head.goto(prev_head.xcor() + 20, prev_head.ycor())
        # screen.update()
        self.square_list.insert(0, new_head)
        self.head = new_head

