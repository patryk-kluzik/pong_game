from turtle import Turtle

SHAPE = 'circle'
COLOUR = 'white'
MOVE_DISTANCE = 5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLOUR)
        self.shape(SHAPE)
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x=x_cor, y=y_cor)

    def bounce(self):
        self.y_move *= -1

    def bounce_back(self):
        self.x_move *= -1