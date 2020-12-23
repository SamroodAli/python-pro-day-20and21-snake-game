"""Main game file"""
from game_screen import screen
from snake import Snake
import turtle

# new Snake instance
snake = Snake()

# event listeners
turtle.onkey(key="w", fun=snake.snake_up)
turtle.onkey(key="a", fun=snake.snake_left)
turtle.onkey(key="s", fun=snake.snake_down)
turtle.onkey(key="d", fun=snake.snake_right)

#starting snake
snake.start_snake()

screen.exitonclick()
