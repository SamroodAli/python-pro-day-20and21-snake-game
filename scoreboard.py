"""Scoreboard module"""
from turtle import Turtle

SCORE_COLOR = "white"
ALIGN = "center"
FONT = ("Courier", 20, "normal")


def read_score():
    """Read previous high score from data.txt"""
    with open("data.txt") as file:
        return int(file.read())


def write_score(high_score):
    """Writes latest high score to data.txt"""
    with open("data.txt",mode="w") as file:
        file.write(str(high_score))


class ScoreBoard(Turtle):
    """Scoreboard class to track score and high score"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_score()
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update scoreboard function"""
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : "
                       f"{self.high_score}", align=ALIGN, font=FONT)

    def add_score(self):
        """Add score function"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Game over function"""
        if self.score > self.high_score:
            self.high_score = self.score
            write_score(self.high_score)
        self.update_scoreboard()
        self.score = 0
        self.goto(0, 0)
        self.color("yellow")
        self.write(arg="GAME OVER\n", align=ALIGN, font=FONT)
        self.goto(0, -100)
        self.write(arg="Press Return [ Enter ]\nfor a new game",align=ALIGN, font=FONT)
