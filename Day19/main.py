from turtle import Turtle, Screen


def move_forwards():
    felix.forward(10)


def move_backwards():
    felix.backward(10)


def turn_left():
    new_heading = felix.heading() + 10
    felix.setheading(new_heading)


def turn_right():
    new_heading = felix.heading() - 10
    felix.setheading(new_heading)


def clear_drawing():
    felix.clear()
    felix.reset()


felix = Turtle()
screen = Screen()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="c", fun=clear_drawing)
screen.exitonclick()
