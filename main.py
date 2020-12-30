from snake_game import SnakeGame
from game_screen import screen
from turtle import onkey

# Init Game instance
snake_game = SnakeGame()


# new game function
def new_game():
    global snake_game
    # accessing the old global snake game to reset screen
    snake_game.reset_screen()
    # new game instance
    snake_game = SnakeGame()


# Event listener for new game
onkey(key="Return", fun=new_game)
snake_game.screen.exitonclick()
