from turtle import Screen
from paddle import Paddle
from turtle import Turtle
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")



paddle_1 = Paddle()
paddle_2 = Paddle(-350, 0)

screen.listen()
screen.onkey(lambda: paddle_1.move_up(), "w")
screen.onkey(lambda: paddle_1.move_down(), "s")

screen.onkey(lambda: paddle_2.move_up(), "Up")
screen.onkey(lambda: paddle_2.move_down(), "Down")





























screen.exitonclick()