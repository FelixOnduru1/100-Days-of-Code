from turtle import Turtle, Screen
import colorgram
import random


def gap(block, size):
    block.penup()
    block.forward(size)
    block.pendown()


def new_line(block):
    block.penup()
    block.setheading(90)
    block.forward(20)
    block.setheading(180)
    block.forward(400)
    block.setheading(0)


colors_raw = colorgram.extract('spots.jpg', 20)
colors = []
for color in colors_raw:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors.append(new_color)

spot_painting = Turtle()
spot_painting.speed("fastest")
screen = Screen()
Screen().colormode(255)
spot_painting.penup()
spot_painting.hideturtle()
spot_painting.setheading(225)
spot_painting.forward(300)
spot_painting.setheading(0)

for _ in range(20):
    for _ in range(20):
        spot_painting.dot(10, random.choice(colors))
        gap(block=spot_painting, size=20)

    new_line(block=spot_painting)

screen.exitonclick()
