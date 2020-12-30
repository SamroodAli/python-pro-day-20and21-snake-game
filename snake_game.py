"""Snake Game file"""
import time
import game_screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
from wall import Wall
from turtle import onkey
# new Snake instance


class SnakeGame:
    def __init__(self):
        self.wall = Wall()
        self.snake = Snake()
        self.scoreboard = ScoreBoard()
        self.food = Food()
        self.screen = game_screen.screen
        self.game_is_on = True
        self.start_game()

# starting snake
    def start_game(self):
        self.game_is_on = True
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.start_snake()
            # Detect collision with food
            if self.snake.head.distance(self.food) < 15:
                self.snake.extend()
                self.food.refresh()
                self.scoreboard.add_score()
            # Detect collision with wall
            x_cor = self.snake.head.xcor()
            y_cor = self.snake.head.ycor()
            if x_cor > 250 or x_cor < -250 or y_cor > 250 or y_cor < -250:
                self.game_is_on = False
                self.scoreboard.game_over()
            # Collision with tail
            for segment in self.snake.snake_body[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.game_is_on = False
                    self.scoreboard.game_over()

