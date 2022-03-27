from turtle import Turtle

# declare some constants
SHAPE = 'circle'
COLOUR = 'white'
START_MOVE_SPEED = 5
FRACTION = 0.9


class Ball(Turtle):

    def __init__(self):
        """
        Object is set up with preset properties.
        It sets up its speed that can be used to update the time.sleep() func.
        """
        super().__init__()
        self.color(COLOUR)
        self.shape(SHAPE)
        self.penup()
        self.x_move = START_MOVE_SPEED
        self.y_move = START_MOVE_SPEED
        self.move_speed = 0.015

    def move(self):
        """
        Method takes the current x & y coordinates and adds the move_speed of the ball object.
        Then the object is moved to the newly updated coordinates.
        """
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x=x_cor, y=y_cor)

    def bounce(self):
        """
        Method sets the y_move to it's inverted value making it move in the opposite vertical direction.
        """
        self.y_move *= -1

    def bounce_back(self):
        """
        Method sets the x_move to it's inverted value making it move in the opposite horizontal direction.
        Move speed is multiplied by a fraction to decrease its value.
        """
        self.x_move *= -1
        self.move_speed *= FRACTION

    def reset_ball(self):
        """
        Reset the ball back to centre of the screen / origin (x=0,y=0).
        Call bounce_back to make the ball travel in the opposite horizontal direction
        and reset the move_speed to its original value.
        """
        self.goto(0, 0)
        self.bounce_back()
        self.move_speed = 0.015
