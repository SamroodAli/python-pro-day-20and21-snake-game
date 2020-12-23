"""Snake continuous movement module"""
import time
from game_screen import SCREEN
import turtle


def start_snake(snake, speed=0.1):
    def turn_east():
        nonlocal snake
        snake[0].setheading(0)
        SCREEN.update()

    def turn_north():
        nonlocal snake
        snake[0].setheading(90)
        SCREEN.update()

    def turn_west():
        nonlocal snake
        snake[0].setheading(180)
        SCREEN.update()

    def turn_south():
        nonlocal snake
        snake[0].setheading(270)
        SCREEN.update()

    turtle.onkey(key="w", fun=turn_north)
    turtle.onkey(key="a", fun=turn_west)
    turtle.onkey(key="s", fun=turn_south)
    turtle.onkey(key="d", fun=turn_east)

    SCREEN.update()
    game_over = False
    while not game_over:
        SCREEN.update()
        time.sleep(speed)
        for index in range(len(snake)-1, 0, -1):
            # snake part at index takes snake part at index-1's position
            new_coordinates = snake[index-1].position()
            snake[index].goto(new_coordinates)
        snake[0].forward(20)
        SCREEN.update()


