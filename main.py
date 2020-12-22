"""Main game file"""
from game_screen import SCREEN
from snake_body import new_snake

snake = new_snake()

SCREEN.exitonclick()
