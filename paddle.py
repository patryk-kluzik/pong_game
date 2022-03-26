from turtle import Turtle

COLOUR = "white"
SHAPE = "square"

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color(COLOUR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y + 20)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y - 20)
