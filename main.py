from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.tracer(0)
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")


l_paddle = Paddle(-390, 0)
r_paddle = Paddle(380, 0)
ball = Ball()


l_score = Scoreboard(-50, 260)
r_score = Scoreboard(50, 260)

screen.listen()

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_dwn, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_dwn, "Down")



line = Turtle()
line.hideturtle()
line.color("white")
line.penup()
line.pensize(3)
line.goto(0, -290)

add = 20
for _ in range(0, 33):
    line.pendown()
    new_y = line.ycor()
    line.goto(0, new_y + add)
    new_y1 = line.ycor()
    line.penup()
    line.goto(0, new_y1 + add)
proceed = True
while proceed:
    # time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    elif ball.xcor() > 400:
        l_score.count()
        ball.refresh()

    elif ball.xcor() < -400:
        r_score.count()
        ball.refresh()

    elif ball.distance(l_paddle) < 40 and ball.xcor() < -380 or (ball.distance(r_paddle) < 40 and ball.xcor() < 390):
        ball.x_bounce()






screen.exitonclick()