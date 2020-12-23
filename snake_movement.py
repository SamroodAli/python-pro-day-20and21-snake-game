"""Snake continous movement module"""
import time
from game_screen import SCREEN


def start_snake(snake, speed=0.1):
    SCREEN.update()
    while True:
        for index in range(0, len(snake)-1):
            next_snake_part_coordinates = snake[index+1].position()
            snake[index].goto(next_snake_part_coordinates)
        snake[-1].forward(20)
        time.sleep(speed)
        SCREEN.update()

