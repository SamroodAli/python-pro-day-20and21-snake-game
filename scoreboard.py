from turtle import Turtle , clear
SCORE_COLOR ="white"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.write(arg=f"Score : {self.score}", align="center", font=("Arial", 25,  "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score}", align="center", font=("Arial", 25, "normal"))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
