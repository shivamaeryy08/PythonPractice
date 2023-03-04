from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
colors = ['red','orange','yellow','green','blue','purple']
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make your bet",prompt="Bet on the turtle that will win the race? Enter a color: ")
y_pos = [100, 60, 20, -20, -60, -100]
all_turtles = []
# xyla.hideturtle()
for i in range(6):
    racing_turtle = Turtle(shape='turtle')
    racing_turtle.color(colors[i])
    racing_turtle.up()
    racing_turtle.goto(x=-230, y=y_pos[i])
    all_turtles.append(racing_turtle)
if bet:
    is_race_on = True

while is_race_on:
    for race_turtle in all_turtles:
        if race_turtle.xcor() > 230:
            winning_color = race_turtle.color()[0]
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle wins!")
            else:
                print(f"You've lost! The {winning_color} turtle wins!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        race_turtle.forward(rand_distance)

screen.exitonclick()

# screen.listen()
#
# racing_turtle = Turtle()
#
# racing_turtle.speed('fastest')
#
#
# def turn_right():
#     racing_turtle.setheading(racing_turtle.heading() - 10)
#
#
# def turn_left():
#     racing_turtle.setheading(racing_turtle.heading() + 10)
#
#
# def move_up():
#     racing_turtle.forward(10)
#
#
# def move_down():
#     racing_turtle.backward(10)
#
#
# def clear():
#     racing_turtle.clear()
#     racing_turtle.up()
#     racing_turtle.setposition(0, 0)
#     racing_turtle.down()
#
#
# screen.onkey(key="w", fun=move_up)  # higher order fx, fx as input, or returns a fucntion
# screen.onkey(key="s", fun=move_down)  # higher order fx, fx as input, or returns a fucntion
# screen.onkey(key="a", fun=turn_left)  # higher order fx, fx as input, or returns a fucntion
# screen.onkey(key="d", fun=turn_right)  # higher order fx, fx as input, or returns a fucntion
# screen.onkey(key="c", fun=clear)
# screen.exitonclick()

# State can mean instance of object has diff states, in terms of attributes or doing a function/method
