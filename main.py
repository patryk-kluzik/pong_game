from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

HEIGHT = 600
WIDTH = 800
PADDING = 15
STARTING_POS = {
    "player_1": (-350, 0),
    "player_2": (350, 0),
}

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

player_1 = Paddle(STARTING_POS["player_1"])
player_2 = Paddle(STARTING_POS["player_2"])

screen.onkeypress(fun=player_1.up, key="w")
screen.onkeypress(fun=player_1.down, key="s")

screen.onkeypress(fun=player_2.up, key="Up")
screen.onkeypress(fun=player_2.down, key="Down")

ball = Ball()

game_over = False
while not game_over:
    time.sleep(0.02)
    screen.update()
    ball.move()

    if ball.ycor() >= HEIGHT/2 - PADDING or ball.ycor() <= -HEIGHT/2 + PADDING:
        ball.bounce()

    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() < -320:
        ball.bounce_back()


screen.exitonclick()
