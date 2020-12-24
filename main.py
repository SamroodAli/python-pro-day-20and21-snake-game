"""Main game file"""
import time

from food import Food
from game_screen import screen
from snake import Snake
from scoreboard import ScoreBoard
# new Snake instance
snake = Snake()
scoreboard = ScoreBoard()
food = Food()
# starting snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.start_snake()
    # Detection collision with food
    if snake.head.distance(food) < 15:
        screen.title("nom nom nom")
        scoreboard.add_score()
        food.move_random()


screen.exitonclick()
