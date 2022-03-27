from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# INIT SOME FINAL VARIABLES
HEIGHT = 600
MAX_HEIGHT = HEIGHT / 2
MIN_HEIGHT = - MAX_HEIGHT
WIDTH = 800
MAX_WIDTH = WIDTH / 2
MIN_WIDTH = - MAX_WIDTH
PADDING = 20
STARTING_POS = {
    "player_1": (-350, 0),
    "player_2": (350, 0),
}

# setup screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

# setup paddle objects
player_1 = Paddle(position=STARTING_POS["player_1"], max_height=MAX_HEIGHT, min_height=MIN_HEIGHT)
player_2 = Paddle(position=STARTING_POS["player_2"], max_height=MAX_HEIGHT, min_height=MIN_HEIGHT)

# setup screen to detect key presses to call paddle methods to move the objects
screen.onkeypress(fun=player_1.up, key="w")
screen.onkeypress(fun=player_1.down, key="s")

screen.onkeypress(fun=player_2.up, key="Up")
screen.onkeypress(fun=player_2.down, key="Down")

# setup ball and score objects
ball = Ball()
score = Score(max_height=MAX_HEIGHT)

game_over = False

while not game_over:
    # sleep updated to move_speed of ball object - lower sleep var means less delay between updates
    time.sleep(ball.move_speed)
    # update screen while all objects have been set up (tracer disables animations)
    screen.update()
    # start the ball to move around the screen
    ball.move()

    # detect if ball goes collides with top and bottom of the screen
    if ball.ycor() >= MAX_HEIGHT - PADDING or ball.ycor() <= MIN_HEIGHT + PADDING:
        # if so, ball bounce with inverts y_axis making ball travel in opposite direction vertically
        ball.bounce()

    # detect if ball is within 50 units of the player/paddle (from the centre to edge of the paddle is 50 units) and
    # check if the ball is between paddle and don't let it bound when its behind paddle
    if ball.distance(player_2) < 50 and 360 > ball.xcor() > 340 or ball.distance(player_1) < 50 \
            and -360 < ball.xcor() < -340:
        ball.bounce_back()

    # check if ball has left the screen, then reset ball and add score for each player
    if ball.xcor() > MAX_WIDTH:
        ball.reset_ball()
        score.add_score_p1()
    elif ball.xcor() < MIN_WIDTH:
        ball.reset_ball()
        score.add_score_p2()

screen.exitonclick()
