from turtle import Turtle
MOVE_PADDLE = 20


class Paddle:

    def __init__(self, x_cor=350, y_cor=0):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.turtle = self.turtle()

    def turtle(self):
        turtle = Turtle()
        turtle.goto(self.x_cor, self.y_cor)
        turtle.shape("square")
        turtle.color("white")
        turtle.shapesize(stretch_wid=5, stretch_len=1)
        turtle.penup()
        return turtle

    def move_up(self):
        self.y_cor += MOVE_PADDLE
        self.turtle.goto(self.x_cor, self.y_cor)

    def move_down(self):
        self.y_cor -= MOVE_PADDLE
        self.turtle.goto(self.x_cor, self.y_cor)

