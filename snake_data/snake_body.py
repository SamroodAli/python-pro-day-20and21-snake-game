"""Snake body"""
from snake_data.snake_body_part import body_part


# initial state
def new_snake(snake_body, no_of_initial_additional_body_parts=3):
    """Returns a new snake with 3 parts at x - coordinates 0 , -20 and -30"""
    x_cor = 0
    for _ in range(no_of_initial_additional_body_parts):
        new_body_part = body_part()
        x_cor -= 20
        new_body_part.setx(x_cor)
        snake_body.append(new_body_part)
    return snake_body