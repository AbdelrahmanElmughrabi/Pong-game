from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



screen=Screen()
screen.listen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r=Paddle(350)
paddle_l=Paddle(-350)
ball=Ball()
scoreboard=Scoreboard()


screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")
screen.onkey(fun=paddle_l.up, key="w")
screen.onkey(fun=paddle_l.down, key="s")

game_is_on=True




while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle_r)<50 and ball.xcor()>320 or ball.distance(paddle_l)<50 and ball.xcor()<-320:
        ball.bounce_x()


    if ball.xcor()>380:
        print("l scored on right panel")
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor()<-380:
        print("r scored on left panel")
        scoreboard.r_point()
        ball.reset_position()

    if ball.xcor()>380:
        ball.reset_position()

    if ball.xcor()<-380:
        ball.reset_position()

screen.exitonclick()