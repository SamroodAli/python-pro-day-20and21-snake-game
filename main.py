"""Main game file"""
from game_screen import SCREEN
from snake_body import new_snake
from snake_movement import start_snake



snake = new_snake()
start_snake(snake)
SCREEN.exitonclick()
