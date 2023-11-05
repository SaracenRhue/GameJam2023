import pygame

color_map = {0: (193, 51, 51), 1: (17, 170, 32), 2: (100, 100, 214)}
black = (0, 0, 0)  # Color for the frame

def draw_color_queue(queue, window, square_size, start_x, start_y, circle_radius):
    spacing = 10  # Spacing between circles
    for i, color_code in enumerate(queue):
        color = color_map[color_code]
        pygame.draw.circle(window, color, (start_x + i * (circle_radius * 2 + spacing), start_y), circle_radius)

def draw_world(queue, world, players, current_player, window, square_size=50 ,dark_mode=False):
    # Define colors
    background_color = (0, 0, 0) if dark_mode else (255, 255, 255)  # Black if dark_mode else white
    frame_color = (255, 255, 255) if dark_mode else (0, 0, 0)
    wall_thickness = 5  # Thickness of the wall lines
    queue_height = square_size  # Height reserved for the color queue

    # Fill background with white
    window.fill(background_color)

    height = len(world)
    width = len(world[0])

    # Draw the outer frame with the correct offset for queue height
    pygame.draw.rect(window, frame_color, (0, queue_height, width * square_size, height * square_size), wall_thickness)

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

    # Define sizes for the top and brim parts of the 'hat' for each player
    brim_height = square_size // 4
    top_height = square_size // 3
    brim_width = square_size - 20
    top_width = square_size - 35

    # Calculate padding for horizontal alignment
    brim_padding_x = (square_size - brim_width) // 2
    top_padding_x = (square_size - top_width) // 2

    # Define y-offset for each player (can be adjusted as needed)
    player0_y_offset = - 10
    player1_y_offset = - 5

    # Draw the brim (player 0)
    player0_cell_x = players[0].x_pos * square_size + brim_padding_x
    player0_cell_y = players[0].y_pos * square_size + queue_height + (3 * square_size // 4) + player0_y_offset
    pygame.draw.rect(window, color_map[players[0].color], (player0_cell_x, player0_cell_y, brim_width, brim_height))

    # Draw the top (player 1)
    player1_cell_x = players[1].x_pos * square_size + top_padding_x
    player1_cell_y = players[1].y_pos * square_size + queue_height + (square_size - top_height) // 2 + player1_y_offset
    pygame.draw.rect(window, color_map[players[1].color], (player1_cell_x, player1_cell_y, top_width, top_height))

    # Outline for the brim if it is the current player's turn
    if current_player == 0:
        pygame.draw.rect(window, frame_color, (player0_cell_x, player0_cell_y, brim_width, brim_height), 2)

    # Outline for the top if it is the current player's turn
    if current_player == 1:
        pygame.draw.rect(window, frame_color, (player1_cell_x, player1_cell_y, top_width, top_height), 2)


    # Draw the color queue
    queue_start_x = square_size // 2  # Start x position for the queue circles
    queue_start_y = square_size // 2  # Start y position for the queue circles (from the top edge of the window)
    circle_radius = square_size // 4  # Radius of the circles in the queue
    
    draw_color_queue(queue.get_queue(), window, square_size, queue_start_x, queue_start_y, circle_radius)

def win(window) -> None:
    print("You won the game")
    win_image = pygame.image.load("img/win.svg")
    window.blit(win_image, win_image.get_rect(center = window.get_rect().center))

def game_over(window) -> None:
    print("You lost the game")
    game_over_image = pygame.image.load("img/game_over.svg")
    window.blit(game_over_image, game_over_image.get_rect(center = window.get_rect().center))
