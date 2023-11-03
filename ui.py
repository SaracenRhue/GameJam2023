import pygame

color_map = {0: (0, 0, 0), 1: (255, 0, 0), 2: (0, 255, 0), 3: (0, 0, 255)}
def draw_world(world, player, window, square_size=50):
    window.fill((0, 0, 0))  # Fill background with black
    for y, row in enumerate(world):
        for x, cell in enumerate(row):
            right_wall, bottom_wall = cell
            # Draw the right wall
            pygame.draw.rect(window, color_map[right_wall], (x * square_size + square_size, y * square_size, square_size, square_size))
            # Draw the bottom wall
            pygame.draw.rect(window, color_map[bottom_wall], (x * square_size, y * square_size + square_size, square_size, square_size))
    
    # Draw a white rectangle at the player's current position
    player_cell_x = player.x_pos * square_size
    player_cell_y = player.y_pos * square_size
    pygame.draw.rect(window, (255, 255, 255), (player_cell_x, player_cell_y, square_size, square_size))

    # Draw the player as a circle on top of the white rectangle
    player_center = (player_cell_x + square_size // 2, player_cell_y + square_size // 2)
    pygame.draw.circle(window, color_map[player.color], player_center, square_size // 2)  # The radius is half the square size
