from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
print(screen.colormode())
felix = Turtle()
felix.shape("turtle")
felix.color(0, 0, 0)

for sides in range(3, 11):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    felix.color(R, G, B)
    for _ in range(sides):
        felix.forward(100)
        felix.right(360/sides)
    for _ in range(sides):
        felix.forward(100)
        felix.left(360/sides)

screen.exitonclick()
