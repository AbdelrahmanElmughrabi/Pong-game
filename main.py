from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Screen setup
screen=Screen()
screen.listen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # Turn off animation updates

# Create game objects
paddle_r=Paddle(350)  # Right paddle
paddle_l=Paddle(-350)  # Left paddle
ball=Ball()
scoreboard=Scoreboard()

# Set up keyboard controls
screen.onkey(fun=paddle_r.up, key="Up")     # Right paddle controls
screen.onkey(fun=paddle_r.down, key="Down")
screen.onkey(fun=paddle_l.up, key="w")      # Left paddle controls
screen.onkey(fun=paddle_l.down, key="s")

game_is_on=True

# Main game loop
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # Update screen manually
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(paddle_r)<50 and ball.xcor()>320 or ball.distance(paddle_l)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # Score points when ball passes paddles
    if ball.xcor()>380:
        print("l scored on right panel")
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor()<-380:
        print("r scored on left panel")
        scoreboard.r_point()
        ball.reset_position()

    # Reset ball position when it goes out of bounds
    if ball.xcor()>380:
        ball.reset_position()

    if ball.xcor()<-380:
        ball.reset_position()

screen.exitonclick()