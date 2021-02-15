from turtle import Turtle, Screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


spirograph = Turtle()
screen = Screen()
Screen().colormode(255)
spirograph.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        difference = i * size_of_gap
        spirograph.color(random_color())
        spirograph.setheading(difference)
        spirograph.circle(100, 360)


draw_spirograph(size_of_gap=5)
screen.exitonclick()
