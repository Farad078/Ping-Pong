from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_paddle(x, y)


    def create_paddle(self, x, y):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 240:
            new_ycor = self.ycor() + 20
            x = self.xcor()
            self.goto(x, new_ycor)

    def move_dwn(self):
        if self.ycor() > -240:
            new_ycor = self.ycor() - 20
            x = self.xcor()
            self.goto(x, new_ycor)


