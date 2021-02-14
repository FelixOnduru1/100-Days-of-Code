from turtle import Turtle, Screen
import random


def north(block):
    block.left(90)
    block.forward(20)
    block.right(90)


def south(block):
    block.right(90)
    block.forward(20)
    block.left(90)


def west(block):
    block.left(180)
    block.forward(20)
    block.right(180)


def east(block):
    block.forward(20)


screen = Screen()
screen.colormode(255)
walk = Turtle()
walk.pensize(width=10)

movement = ["north", "east", "west", "south"]

for _ in range(200):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    walk.color(R, G, B)
    walk.hideturtle()
    random_movement = random.choice(movement)

    if random_movement == "north":
        north(block=walk)
    elif random_movement == "south":
        south(block=walk)
    elif random_movement == "west":
        west(block=walk)
    elif random_movement == "east":
        east(block=walk)


screen.exitonclick()
