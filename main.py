"""Main game file"""
from game_screen import screen
from snake import Snake
from food import Food
import turtle

# new Snake instance
snake = Snake()
food = Food()
# event listeners
turtle.onkey(key="w", fun=snake.snake_up)
turtle.onkey(key="a", fun=snake.snake_left)
turtle.onkey(key="s", fun=snake.snake_down)
turtle.onkey(key="d", fun=snake.snake_right)

# starting snake
snake.start_snake()

screen.exitonclick()
