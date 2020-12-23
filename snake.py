from snake_data.snake_body import new_snake
from snake_data.snake_movement import move


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_new_snake()

    def create_new_snake(self):
        self.snake_body = new_snake(self.snake_body)

    def start_snake(self, speed=0.1):
        move(self.snake_body, speed)




