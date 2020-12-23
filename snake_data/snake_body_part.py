"""Snake body part module"""
from turtle import Turtle


def body_part(turtle=Turtle):
    """returns a new snake body part"""
    snake_part = turtle(shape="square")
    snake_part.color("white")
    snake_part.penup()
    snake_part.speed(0)
    return snake_part
