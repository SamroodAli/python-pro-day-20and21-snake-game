"""Snake continuous movement module"""
import time
from game_screen import screen


def move(snake, speed):
    screen.update()
    game_over = False
    while not game_over:
        screen.update()
        time.sleep(speed)
        for index in range(len(snake)-1, 0, -1):
            # snake part at index takes snake part at index-1's position
            new_coordinates = snake[index-1].position()
            snake[index].goto(new_coordinates)
        snake[0].forward(20)
        screen.update()


