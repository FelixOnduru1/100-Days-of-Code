import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_image.gif"
screen.addshape(img)
turtle.shape(img)
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guessed_state = []
game_active = True

while game_active:
    answer_state = screen.textinput(title=f"Guess a State. {len(guessed_state)}/50", prompt="Type a state name").title()

    if len(guessed_state) > 50 or answer_state == "Exit":
        missed_state = [state for state in states if state not in guessed_state]
        missed_state_data = pd.DataFrame(missed_state)
        missed_state_data.to_csv("missed_states.csv")
        game_active = False
        break

    if answer_state in states and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        xcor = int(state_data.x)
        ycor = int(state_data.y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(xcor, ycor)
        t.write(answer_state)
