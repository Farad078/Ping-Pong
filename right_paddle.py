from turtle import Turtle

class Right_Paddle:
    def __init__(self):
        self.paddles = []
        self.create_paddle()

    def create_paddle(self):
        paddle = Turtle()
        paddle.color("white")
        paddle.shape("square")
        paddle.shapesize(stretch_wid=4, stretch_len=0.7)
        paddle.penup()
        paddle.goto(380, 0)
        self.paddles.append(paddle)

    def move(self):
        self.paddles[0].fd(40)
