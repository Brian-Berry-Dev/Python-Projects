from turtle import Turtle
import random

pos = [-260, -240, -220, ]

control = -260
for _ in range(1, 28):
    pos.append(control)
    control += 20


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.turtlesize(.8)
        self.penup()

    def create(self):
        ran_x = random.choice(pos)
        ran_y = random.choice(pos)
        print(f"food pos = x {ran_x} y {ran_y} ")
        self.goto(ran_x, ran_y)
        return self.pos()

    def check_food(self):
        return self.pos()
