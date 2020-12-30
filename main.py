"""Main File"""
from snake_game import SnakeGame
from turtle import onkey
# Init Game instance
new_snake_game = SnakeGame()


# new game function
def new_game():
    """New game and old game screen reset"""
    global new_snake_game
    # accessing the old global snake game to reset screen
    new_snake_game.screen.resetscreen()
    # new game instance
    new_snake_game = SnakeGame()


# Event listener for new game
onkey(key="Return", fun=new_game)
new_snake_game.screen.exitonclick()
