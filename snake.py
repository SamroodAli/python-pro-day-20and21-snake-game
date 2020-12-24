from turtle import Turtle, onkey
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SNAKE_COLOR = "white"
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_new_snake()
        self.head = self.snake_body[0]
        self.setup_direction_event_listeners()

    def create_new_snake(self):
        """Returns a new snake with 3 parts at x - coordinates 0 , -20 and -30"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extend(self):
        pass

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
