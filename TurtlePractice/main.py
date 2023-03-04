import turtle
from turtle import Turtle, Screen
import random
import colorgram

# from turtle import * means import everything
# import turtle as t aliasing module
xyla_turtle = Turtle()
xyla_turtle.shape('turtle')
xyla_turtle.color("red")
x = 4


# for _ in range(4):
#     xyla_turtle.forward(100)
#     xyla_turtle.right(90)

# for _ in range(15):
#     xyla_turtle.down()
#     xyla_turtle.forward(10)
#     xyla_turtle.up()
#     xyla_turtle.forward(10)


#
#

def create_random_rgb():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_poly(sides):
    angle = 360 / sides
    for _ in range(sides):
        xyla_turtle.color(random.choice(create_random_rgb()))
        xyla_turtle.forward(100)
        xyla_turtle.right(angle)


# def generate_shapes():
#     for i in range(3, 11):
#         draw_poly(i)
#

# generate_shapes()


turtle.colormode(255)


def move_turtle(movement_direction, distance, width):
    xyla_turtle.color(create_random_rgb())
    xyla_turtle.speed('fastest')
    xyla_turtle.width(width)
    if movement_direction == "right":
        xyla_turtle.right(90)
        xyla_turtle.forward(distance)
    elif movement_direction == "left":
        xyla_turtle.left(90)
        xyla_turtle.forward(distance)
    elif movement_direction == "forward":
        xyla_turtle.forward(distance)
    else:
        xyla_turtle.backward(distance)


# movement = ['forward', 'backward', 'right', 'left']
# for _ in range(200):
#     movement_choice = random.choice(movement)
#     move_turtle(movement_choice, 50, 5)
# print(create_random_rgb())

# tuples are immutable, lists mutable, dicts mutable
xyla_turtle.speed('fastest')


def create_spherical(radius, tilt):
    xyla_turtle.color(create_random_rgb())
    xyla_turtle.circle(radius)
    xyla_turtle.left(tilt)


# for _ in range(36):
#     create_spherical(100, 10)
def get_color(color_obj):
    return color_obj.rgb.r, color_obj.rgb.g, color_obj.rgb.b


# colors = map(get_color, colorgram.extract('image.jpg', 34))
# print(list(colors))
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

color_number = 0

# def get_next_color(list_colors):
#     global color_number
#     if color_number == len(color_list):
#         color_number = 0
#     color = list_colors[color_number]
#     color_number += 1
#     return color

def create_spot_painting(dot_size, number_rows, number_columns, gap_rows):
    xyla_turtle.hideturtle()
    xyla_turtle.pencolor('white')
    xyla_turtle.setheading(220)
    xyla_turtle.forward(500)
    xyla_turtle.setheading(0)
    for i in range(number_rows):
        cur_pos = xyla_turtle.pos()
        for j in range(number_columns):
            xyla_turtle.down()
            xyla_turtle.fillcolor(random.choice(color_list))
            xyla_turtle.begin_fill()
            xyla_turtle.circle(dot_size)
            xyla_turtle.end_fill()
            xyla_turtle.up()
            xyla_turtle.forward(80)

        xyla_turtle.setx(cur_pos[0])
        xyla_turtle.sety(cur_pos[1] + gap_rows)


create_spot_painting(15, 10, 10, 80)

screen = Screen()
screen.exitonclick()
