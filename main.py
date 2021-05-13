from turtle import Screen
from paddle import Paddle
from turtle import Turtle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle()
paddle_left = Paddle(-350, 0)

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

ball = Ball()

game_on = True
while game_on:

    screen.update()
    ball.move()
    print(ball.ycor())

    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 340 or ball.distance(paddle_left) < 50 and ball.xcor() < -340:
        ball.bounce_x()

screen.exitonclick()
