import pygame

color_map = {0: (255, 0, 0), 1: (0, 255, 0), 2: (0, 0, 255)}
black = (0, 0, 0)  # Color for the frame

def draw_world(world, player, window, square_size=50):
    # Define colors
    background_color = (255, 255, 255)  # White
    wall_thickness = 5  # Thickness of the wall lines
    
    # Fill background with white
    window.fill(background_color)

    height = len(world)
    width = len(world[0])

    # Draw the outer frame
    pygame.draw.rect(window, black, (0, 0, width * square_size, height * square_size), wall_thickness)
    
    # Draw the grid lines (walls)
    for y in range(height):
        for x in range(width):
            right_wall, bottom_wall = world[y][x]
            
            # Draw the right wall if it's not the rightmost cell
            if x < width - 1:
                right_wall_start = (x * square_size + square_size, y * square_size)
                right_wall_end = (x * square_size + square_size, y * square_size + square_size)
                pygame.draw.line(window, color_map[right_wall], right_wall_start, right_wall_end, wall_thickness)
            
            # Draw the bottom wall if it's not the bottommost cell
            if y < height - 1:
                bottom_wall_start = (x * square_size, y * square_size + square_size)
                bottom_wall_end = (x * square_size + square_size, y * square_size + square_size)
                pygame.draw.line(window, color_map[bottom_wall], bottom_wall_start, bottom_wall_end, wall_thickness)

    # Draw the player
    player_cell_x = player.x_pos * square_size
    player_cell_y = player.y_pos * square_size
    player_center = (player_cell_x + square_size // 2, player_cell_y + square_size // 2)
    # Draw the player as a circle on top of the grid
    pygame.draw.circle(window, color_map[player.color], player_center, square_size // 4)  # The radius is a quarter of the square size
