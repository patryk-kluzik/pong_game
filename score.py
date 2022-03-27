from turtle import Turtle

# set some constants
COLOUR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 75, "normal")
PADDING_FOR_SCORE = 120


class Score(Turtle):

    def __init__(self, max_height):
        """
        Declare new score object. Set up some properties of the score object and set up default
        scores to 0. Call update_score() to write the score to the screen.
        :param max_height: int representing top of the screen (highest y co-ord)
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(COLOUR)
        self.p1_score = 0
        self.p2_score = 0
        self.score_y_cord = max_height - PADDING_FOR_SCORE
        self.update_score()

    def update_score(self):
        """
        Clear the screen to remove any previous text.
        Take the object to the top of the score_y_cord (top of the screen - padding)
        and write the current object attributes of score for p1 and p2.
        """
        self.clear()
        self.goto(x=0, y=self.score_y_cord)
        self.write(arg=f"{self.p1_score} : {self.p2_score}", align=ALIGNMENT, font=FONT)

    def add_score_p1(self):
        """
        Increase the player_1 score by 1 and call update_score to write new score to the screen.
        """
        self.p1_score += 1
        self.update_score()

    def add_score_p2(self):
        """
        Increase the player_2 score by 1 and call update_score to write new score to the screen.
        """
        self.p2_score += 1
        self.update_score()
