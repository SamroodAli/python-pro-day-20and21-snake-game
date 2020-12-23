from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def move_random(self):
        x = randint(0, 280)
        y = randint(0, 280)
        self.goto(x, y)