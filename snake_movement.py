"""Snake continuous movement module"""
import time
from game_screen import SCREEN
import turtle


def start_snake(snake, speed=0.2):
    def turn_right():
        nonlocal snake
        snake[-1].right(90)
        SCREEN.update()

    def turn_left():
        nonlocal snake
        snake[-1].left(90)
        SCREEN.update()

    turtle.onkey(key="d", fun=turn_right)
    turtle.onkey(key="a", fun=turn_left)

    SCREEN.update()
    game_over = False
    while not game_over:
        for index in range(0, len(snake)-1):
            next_snake_part_coordinates = snake[index+1].position()
            snake[index].goto(next_snake_part_coordinates)
        snake[-1].forward(20)
        time.sleep(speed)
        SCREEN.update()


