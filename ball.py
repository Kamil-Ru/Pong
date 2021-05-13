from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, direct):
        new_x = self.xcor() + 0.01
        if direct == "down":
            new_y = self.ycor() - 0.5
        elif direct == "up":
            new_y = self.ycor() + 0.1
        else:
            new_y = self.ycor()
        self.goto(new_x, new_y)

    def border_check(self, direc):
        if self.ycor() > 290:
            return "down"
        elif self.ycor() < -290:
            return "up"
        else:
            return direc