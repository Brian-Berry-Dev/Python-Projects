from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", True, align="center", font=('Arial', 15, 'normal'))

    def plus_1(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align="center", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0, 50)
        self.color("red")
        self.write("GAME OVER", True, align="center", font=('Arial', 55, 'bold'))
