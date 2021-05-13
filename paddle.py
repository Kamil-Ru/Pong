from turtle import Turtle
MOVE_PADDLE = 20


class Paddle(Turtle):

    def __init__(self, x_cor=350, y_cor=0):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.goto(self.x_cor, self.y_cor)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def move_up(self):
        self.y_cor += MOVE_PADDLE
        self.goto(self.x_cor, self.y_cor)

    def move_down(self):
        self.y_cor -= MOVE_PADDLE
        self.goto(self.x_cor, self.y_cor)

