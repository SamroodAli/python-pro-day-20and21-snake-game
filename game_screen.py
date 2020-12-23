"""game screen settings"""
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")

# Animation off  settings
screen.tracer(0)
# screen set up to listen for key events
screen.listen()
