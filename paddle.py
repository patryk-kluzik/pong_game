from turtle import Turtle

# declare some constants
COLOUR = "white"
SHAPE = "square"
PADDING_FROM_CENTRE = 40
MOVE_SPEED = 50


class Paddle(Turtle):

    def __init__(self, position, max_height, min_height):
        """
        Create a new paddle object. Set up its properties and position

        :param position: tuple of x and y co-ords to set up position on the paddle
        :param max_height: int representing top of the screen (highest y co-ord)
        :param min_height: int representing bottom of the screen (lowest y co-ord)
        """
        super().__init__()
        self.max_height = max_height
        self.min_height = min_height
        self.penup()
        self.color(COLOUR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def up(self):
        """
        Function takes objects current y co-ord and adds constant amount to it (making it go up in the y-axis).
        Check if the new y co-ord ( plus padding due to coord originating from objects centre) is less than the
        max_height, then move paddle to the new y_axis.
        """
        new_y = self.ycor() + MOVE_SPEED
        if new_y + PADDING_FROM_CENTRE < self.max_height:
            self.goto(x=self.xcor(), y=new_y)

    def down(self):
        """
        Function takes objects current y co-ord and subtract constant amount from it (making it go down in the y-axis).
        Check if the new y co-ord ( minus padding due to coord originating from objects centre) is more than the
        min_height, then move paddle to the new y_axis.
        """
        new_y = self.ycor() - MOVE_SPEED
        if new_y - PADDING_FROM_CENTRE > self.min_height:
            self.goto(x=self.xcor(), y=new_y)
