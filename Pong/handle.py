from turtle import Turtle

UP = 90
DISTANCE = 20
DOWN = 270


class Handle():
    def __init__(self, location):
        head = Turtle('square')
        head.color('white')
        self.segment_list = [head]
        self.head = head
        self.location = location
        self.generate_handle()

    def move(self, window_height):
        if self.location == 'left' and self.head.ycor() > window_height / 2 - 70 and self.head.heading() == UP:
            pass
        elif self.location == 'left' and self.head.ycor() < -1 * (
                window_height / 2) + 70 and self.head.heading() == DOWN:
            pass
        else:
            for i in range(len(self.segment_list) - 1, 0, -1):
                cur_square = self.segment_list[i]
                pos_mov_to = self.segment_list[i - 1].position()
                cur_square.goto(pos_mov_to)
            self.head.forward(DISTANCE)

    def go_down(self):
        self.head.setheading(DOWN)

    def go_up(self):
        self.head.setheading(UP)

    def generate_handle(self):
        for i in range(5):
            prev_head = self.head
            new_head = Turtle('square')
            new_head.color('white')
            new_head.penup()
            new_head.goto(prev_head.xcor(), prev_head.ycor() + 20)
            self.head = new_head
            self.segment_list.insert(0, new_head)
        self.head.setheading(UP)

    def set_location(self, window_width):
        if self.location == 'left':
            for segments in self.segment_list:
                segments.penup()
                segments.goto(segments.xcor() - (window_width / 2.2), segments.ycor())
        else:
            for segments in self.segment_list:
                segments.penup()
                segments.goto(segments.xcor() + (window_width / 2.2), segments.ycor())

    def move_up_and_down(self, window_height):
        if self.head.ycor() > window_height / 2 - 70:
            self.go_down()
        elif self.head.ycor() < (-1 * (window_height / 2)) + 70:
            self.go_up()
        self.move(window_height=window_height)
