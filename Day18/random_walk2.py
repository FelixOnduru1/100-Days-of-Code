from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
walk = Turtle()
walk.pensize(width=10)

direction = [0, 90, 180, 270]

for _ in range(200):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    walk.color(R, G, B)
    walk.hideturtle()
    walk.forward(20)
    walk.setheading(random.choice(direction))
screen.exitonclick()
