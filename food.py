"""Food class"""
from turtle import Turtle
from random import randint


class Food(Turtle):
    """Food class"""
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    # place food randomly
    def refresh(self):
        """Random food placement"""
        x_cor = randint(0, 245)
        y_cor = randint(0, 245)
        self.goto(x_cor, y_cor)
