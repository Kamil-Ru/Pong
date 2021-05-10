from turtle import Turtle


class Paddle:

    def __init__(self, x_pos=350, y_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.turtle = self.turtle()

    def turtle(self):
        turtle = Turtle()
        turtle.goto(self.x_pos, self.y_pos)
        turtle.shape("square")
        turtle.color("white")
        turtle.shapesize(stretch_wid=5, stretch_len=1)
        turtle.penup()
        return turtle

    def move_up(self):
        self.y_pos += 10
        self.turtle.goto(self.x_pos, self.y_pos)

    def move_down(self):
        self.y_pos -= 10
        self.turtle.goto(self.x_pos, self.y_pos)

