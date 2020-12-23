"""game screen settings"""
from turtle import Screen

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.title("My Snake Game")
SCREEN.bgcolor("black")

# Animation off  settings
SCREEN.tracer(0)
# screen set up to listen for key events
SCREEN.listen()
