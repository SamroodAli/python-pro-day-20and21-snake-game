from turtle import Turtle
SCORE_COLOR ="white"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(SCORE_COLOR)