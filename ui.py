import pygame

color_map = {0: (255, 0, 0), 1: (0, 255, 0), 2: (0, 0, 255)}
black = (0, 0, 0)  # Color for the frame

def draw_color_queue(queue, window, square_size, start_x, start_y, circle_radius):
    spacing = 10  # Spacing between circles
    for i, color_code in enumerate(queue):
        color = color_map[color_code]
        pygame.draw.circle(window, color, (start_x + i * (circle_radius * 2 + spacing), start_y), circle_radius)

def draw_world(world, player, window, square_size=50):
    # Define colors
    background_color = (255, 255, 255)  # White
    wall_thickness = 5  # Thickness of the wall lines
    queue_height = square_size  # Height reserved for the color queue

    # Fill background with white
    window.fill(background_color)

    height = len(world)
    width = len(world[0])

    # Draw the outer frame with the correct offset for queue height
    pygame.draw.rect(window, black, (0, queue_height, width * square_size, height * square_size), wall_thickness)

    # Draw the grid lines (walls) with the correct offset for queue height
    for y in range(height):
        for x in range(width):
            right_wall, bottom_wall = world[y][x]
            
            # Draw the right wall if it's not the rightmost cell
            if x < width - 1:
                right_wall_start = (x * square_size + square_size, y * square_size + queue_height)
                right_wall_end = (x * square_size + square_size, y * square_size + square_size + queue_height)
                pygame.draw.line(window, color_map[right_wall], right_wall_start, right_wall_end, wall_thickness)
            
            # Draw the bottom wall if it's not the bottommost cell
            if y < height - 1:
                bottom_wall_start = (x * square_size, y * square_size + square_size + queue_height)
                bottom_wall_end = (x * square_size + square_size, y * square_size + square_size + queue_height)
                pygame.draw.line(window, color_map[bottom_wall], bottom_wall_start, bottom_wall_end, wall_thickness)

    # Draw the player
    player_cell_x = player.x_pos * square_size
    player_cell_y = player.y_pos * square_size + queue_height
    player_center = (player_cell_x + square_size // 2, player_cell_y + square_size // 2)
    pygame.draw.circle(window, color_map[player.color], player_center, square_size // 4)  # The radius is a quarter of the square size

    # Draw the color queue
    queue_start_x = square_size // 2  # Start x position for the queue circles
    queue_start_y = square_size // 2  # Start y position for the queue circles (from the top edge of the window)
    circle_radius = square_size // 4  # Radius of the circles in the queue
    
    draw_color_queue(player.color_queue, window, square_size, queue_start_x, queue_start_y, circle_radius)
