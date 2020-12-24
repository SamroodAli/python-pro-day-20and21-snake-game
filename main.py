"""Main game file"""
import time

from food import Food
from game_screen import screen
from snake import Snake
from scoreboard import ScoreBoard
from wall import Wall
# new Snake instance
wall = Wall()
snake = Snake()
scoreboard = ScoreBoard()
food = Food()
# starting snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.start_snake()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.add_score()

    # Detect collision with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > 250 or x_cor < -250 or y_cor > 250 or y_cor < -250:
        game_is_on = False
        scoreboard.game_over()

    # Collision with tail
    for segment in snake.snake_body:
        if segment != snake.head and snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
