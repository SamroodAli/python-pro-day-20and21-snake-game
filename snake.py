from snake_data.snake_body import new_snake
from snake_data.snake_movement import move
from game_screen import screen

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_new_snake()

    def create_new_snake(self):
        self.snake_body = new_snake(self.snake_body)

    def start_snake(self, speed=0.1):
        move(self.snake_body, speed)

    def snake_right(self):
        self.snake_body[0].setheading(0)

    def snake_up(self):
        self.snake_body[0].setheading(90)

    def snake_left(self):
        self.snake_body[0].setheading(180)

    def snake_down(self):
        self.snake_body[0].setheading(270)
