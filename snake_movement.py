"""Snake continuous movement module"""
import time
from game_screen import SCREEN
import turtle


def start_snake(snake, speed=0.1):
    def turn_east():
        nonlocal snake
        snake[-1].setheading(0)
        SCREEN.update()

    def turn_north():
        nonlocal snake
        snake[-1].setheading(90)
        SCREEN.update()

    def turn_west():
        nonlocal snake
        snake[-1].setheading(180)
        SCREEN.update()

    def turn_south():
        nonlocal snake
        snake[-1].setheading(270)
        SCREEN.update()

    turtle.onkey(key="w", fun=turn_north)
    turtle.onkey(key="a", fun=turn_west)
    turtle.onkey(key="s", fun=turn_south)
    turtle.onkey(key="d", fun=turn_east)

    SCREEN.update()
    game_over = False
    while not game_over:
        for index in range(0, len(snake)-1):
            next_snake_part_coordinates = snake[index+1].position()
            snake[index].goto(next_snake_part_coordinates)
        snake[-1].forward(20)
        time.sleep(speed)
        SCREEN.update()


