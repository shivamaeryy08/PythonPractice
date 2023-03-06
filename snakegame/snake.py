from turtle import Turtle

segment = Turtle('square')
segment.color('white')
segment.penup()
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment_list = [segment]
        self.head = segment
        self.tail = segment

    def move(self):
        for i in range(len(self.segment_list) - 1, 0, -1):
            cur_square = self.segment_list[i]
            pos_mov_to = self.segment_list[i - 1].position()
            cur_square.goto(pos_mov_to)
        self.head.forward(DISTANCE)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
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
        new_head.color('white')
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
        self.segment_list.insert(0, new_head)
        self.head = new_head

    def detect_collision(self, window_width, window_height, distance_boundary):
        out_bounds = self.head.xcor() > window_width / 2 - distance_boundary or self.head.xcor() < (
                -1 * (
                window_width / 2 - distance_boundary)) or self.head.ycor() > window_height / 2 - distance_boundary or self.head.ycor() < (
                             -1 * (window_height / 2 - distance_boundary))
        collided_tail = False
        for snake_segment in self.segment_list[1:]:
            if self.head.distance(snake_segment) < 5:
                collided_tail = True
        return collided_tail or out_bounds
