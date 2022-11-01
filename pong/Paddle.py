from turtle import Turtle

MOVE_DISTANCE = 10

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos, 0)

    def up(self):
        y = self.ycor()
        y += 25
        self.sety(y)

    def down(self):
        y = self.ycor()
        y -= 25
        self.sety(y)