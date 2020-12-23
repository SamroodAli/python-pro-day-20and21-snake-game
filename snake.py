from snake_data.snake_body import new_snake
from snake_data.snake_movement import move
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_new_snake()
        self.head = self.snake_body[0]

    def create_new_snake(self):
        # from snake data folder , new snake function
        self.snake_body = new_snake(self.snake_body)

    def start_snake(self, speed=0.1):
        # from snake data folder - module snake movement
        move(self.snake_body, speed)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
