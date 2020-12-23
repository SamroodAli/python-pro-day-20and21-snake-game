from turtle import Turtle, onkey
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
NO_OF_INITIAL_BODY_PARTS = 3
SNAKE_COLOR = "white"


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_new_snake()
        self.head = self.snake_body[0]

    def create_new_snake(self):
        """Returns a new snake with 3 parts at x - coordinates 0 , -20 and -30"""
        x_cor = 0
        for _ in range(NO_OF_INITIAL_BODY_PARTS):
            new_body_part = Turtle(shape="square")
            new_body_part.color(SNAKE_COLOR)
            new_body_part.penup()
            new_body_part.speed(0)
            x_cor -= 20
            new_body_part.setx(x_cor)
            self.snake_body.append(new_body_part)

    # snake movement method
    def start_snake(self):
        for index in range(len(self.snake_body) - 1, 0, -1):
            # snake part at index takes snake part at index-1's position
            new_coordinates = self.snake_body[index - 1].position()
            self.snake_body[index].goto(new_coordinates)
        self.head.forward(20)

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

    def setup_direction_event_listeners(self):
        onkey(key="w", fun=self.snake_up)
        onkey(key="a", fun=self.snake_left)
        onkey(key="s", fun=self.snake_down)
        onkey(key="d", fun=self.snake_right)
