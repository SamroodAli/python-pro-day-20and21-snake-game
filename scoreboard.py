from turtle import Turtle

SCORE_COLOR = "white"
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()
        self.score = 0
        self.goto(0, 0)
        self.color("yellow")
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
