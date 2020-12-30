"""game screen settings"""
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")

# turning animation off
screen.tracer(0)
# listening for key press events
screen.listen()
