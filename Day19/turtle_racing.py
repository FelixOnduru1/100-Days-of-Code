from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
race_active = False
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for idx in range(6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[idx])
    y_position = -90 + (idx * 40)
    new_turtle.goto(-230, y_position)
    turtles.append(new_turtle)

if user_bet:
    race_active = True

while race_active:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_active = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The winner of the race is the {winning_color} turtle.")
            else:
                print(f"You lose! The winner of the race is the {winning_color} turtle.")

        else:
            random_distance = random.randint(1, 10)
            turtle.forward(random_distance)

screen.exitonclick()
