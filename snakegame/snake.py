from turtle import Turtle

square = Turtle('square')
square.color('white')
square.penup()
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# TODO make distance bet squares cusotmizatbale
# TODO fix snake measurement w.r to hitting circle
# TODO fix snake speed

class Snake:

    def __init__(self):
        self.square_list = [square]
        self.head = square
        self.tail = square

    # self.head.speed('normal')
    # self.add_head()
    # self.add_head()
    # self.add_head()
    # self.add_head()
    # self.add_head()
    # self.add_head()

    def move(self):
        for i in range(len(self.square_list) - 1, 0, -1):
            cur_square = self.square_list[i]
            pos_mov_to = self.square_list[i - 1].position()
            cur_square.goto(pos_mov_to)
        self.head.forward(DISTANCE)
        if (self.detect_collision()):
            print("head hit tail")

    def turn_right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def turn_left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def add_head(self):
        prev_head = self.head
        new_head = Turtle('square')
        new_head.hideturtle()
        new_head.color('white')
        new_head.speed('fastest')
        new_head.penup()
        new_head.setheading(prev_head.heading())
        if prev_head.heading() == UP:
            new_head.goto(prev_head.xcor(), prev_head.ycor() + 20)
        elif prev_head.heading() == DOWN:
            new_head.goto(prev_head.xcor(), prev_head.ycor() - 20)
        elif prev_head.heading() == LEFT:
            new_head.goto(prev_head.xcor() - 20, prev_head.ycor())
        else:
            new_head.goto(prev_head.xcor() + 20, prev_head.ycor())
        new_head.showturtle()
        self.square_list.insert(0, new_head)
        self.head = new_head

    def detect_collision(self):
        return self.head.distance(self.tail) < 15
