import turtle
import pandas
from Score import Score
import time

ALIGNMENT = "center"
FONT = ('Arial', 8, 'normal')

screen = turtle.Screen()
screen.tracer(0, 0)
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
score = Score()
screen.update()
game_active = True

data = pandas.read_csv('50_states.csv')

list_states = data['state'].to_list()


def write_state(x_coord, y_coord, state):
    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.goto(x_coord, y_coord)
    state_turtle.write(arg=f'{state}', font=FONT)
    score.update_score()
    screen.update()
    time.sleep(1)


def check_answer(user_answer):
    user_answer = user_answer.title()
    if not (user_answer in list_states):
        print("No state found")
        time.sleep(1)
        return
    x_coord = data[data['state'] == user_answer]['x'].to_list()[0]
    y_coord = data[data['state'] == user_answer]['y'].to_list()[0]
    write_state(x_coord=x_coord, y_coord=y_coord, state=user_answer)


while game_active:
    answer = screen.textinput(title="Guess the state", prompt="Guess a state name")
    check_answer(user_answer=answer)
    if score.score == 50:
        game_active = False
