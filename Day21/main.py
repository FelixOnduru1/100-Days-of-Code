# TODO: 1 Create the screen
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time
game_active = True
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
# TODO: 2 Create and move the paddle
paddle_A = Paddle(position=(-350, 0))
paddle_B = Paddle(position=(350, 0))
ball = Ball()
scoreboard = Scoreboard()
while game_active:
    scoreboard.update_scoreboard()
    screen.update()
    time.sleep(0.1)
    ball.move()
    screen.listen()

    screen.onkeypress(key="w", fun=paddle_A.up)
    screen.onkeypress(key="s", fun=paddle_A.down)
    screen.onkeypress(key="Up", fun=paddle_B.up)
    screen.onkeypress(key="Down", fun=paddle_B.down)
# TODO: 3 Create another paddle
# TODO: 4 Create the ball and make it move
# TODO: 5 Detect collision with wall and bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# TODO: 6 Detect collision with paddle
    if ball.distance(paddle_B) < 50 and ball.xcor() > 330 or ball.distance(paddle_A) < 50 and ball.xcor() < -330:
        ball.bounce_x()
# TODO: 7 Detect when paddle misses ball
    # paddle_B missing
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.point_a()
    # paddle_A missing
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.point_b()
# TODO: 8 Keep score
screen.exitonclick()
