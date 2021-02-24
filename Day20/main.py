from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Snake Game")

screen.tracer(0)
game_active = True
# TODO: 1. Create a snake body
snake = Snake()
food = Food()
# TODO: 3. Create Snake food
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
# TODO: 2. Move the Snake
while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move()

# TODO: 4. Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
# TODO: 5. Create a scoreboard
        scoreboard.increase_score()


# TODO: 6 Detection collision with wall
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
# TODO: 7. Detection collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
