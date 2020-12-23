"""Main game file"""
import turtle
import time

from food import Food
from game_screen import screen
from snake import Snake

# new Snake instance
snake = Snake()

# event listeners
snake.setup_direction_event_listeners()

food = Food()
# starting snake
game_is_on = True
food.move_random()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.start_snake()


screen.exitonclick()
