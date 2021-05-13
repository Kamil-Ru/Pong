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

paddle_left = Paddle()
paddle_right = Paddle(-350, 0)

screen.listen()
screen.onkey(paddle_left.move_up, "Up")
screen.onkey(paddle_left.move_down, "Down")

screen.onkey(paddle_right.move_up, "w")
screen.onkey(paddle_right.move_down, "s")

ball = Ball()

direction = "down"
game_on = True
while game_on:
    screen.update()
    ball.move(direction)
    direction = ball.border_check(direction)

    # if ball.distance(paddle_left) < 50 or ball.xcor() > 340:
    #     print("bla")


screen.exitonclick()