"""Main game file"""
from game_screen import SCREEN
from snake import Snake


snake = Snake()
snake.start_snake()
SCREEN.exitonclick()
