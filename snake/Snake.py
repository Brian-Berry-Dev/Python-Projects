from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_body(pos)

    def add_body(self, position):
        snek = Turtle(shape="square")
        snek.color("white")
        snek.penup()
        snek.goto(position)
        self.snake.append(snek)

    def extend_body(self):
        self.add_body(self.snake[-1].position())

    def snake_move(self):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            self.snake[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def check_head(self):
        return self.head.pos()

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
