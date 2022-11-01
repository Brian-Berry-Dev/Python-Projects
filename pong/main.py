from turtle import Screen
from Ball import Ball
from Paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
paddle_left = Paddle(-420)
paddle_right = Paddle(420)
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")
screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")






game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    print(ball.xcor())

    if ball.ycor() > 320 or ball.ycor() < -320:
        ball.bounce_y()

    if ball.xcor() > 390:
        if paddle_right.distance(ball) < 50:
            ball.bounce_x()
            ball.speed()
        else:
            scoreboard.l_point()
            ball.ball_reset()

    if ball.xcor() < -390:
        if paddle_left.distance(ball) < 50:
            ball.bounce_x()
            ball.speed()
        else:
            scoreboard.r_point()
            ball.ball_reset()
            ball.move()



