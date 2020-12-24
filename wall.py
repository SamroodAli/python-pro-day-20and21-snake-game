from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.create_wall()

    def create_wall(self):
        self.color("yellow")
        self.penup()
        self.goto(250, 250)
        self.pendown()
        self.goto(250, -250)
        self.goto(-250, -250)
        self.goto(-250, 250)
        self.goto(250, 250)
        self.hideturtle()
