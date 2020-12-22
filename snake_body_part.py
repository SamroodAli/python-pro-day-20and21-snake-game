"""Snake body part module"""
from turtle import Turtle


def body_part():
    """returns a new snake body part"""
    snake_part = Turtle(shape="square")
    snake_part.color("white")
    snake_part.penup()
    return snake_part
