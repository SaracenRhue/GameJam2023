import pygame

color_map = {0: (193, 51, 51), 1: (17, 170, 32), 2: (100, 100, 214)}
black = (0, 0, 0)  # Color for the frame

def draw_arrow(
        surface: pygame.Surface,
        start: pygame.Vector2,
        end: pygame.Vector2,
        color: pygame.Color,
        body_width: int = 2,
        head_width: int = 4,
        head_height: int = 2,
    ):
    """Draw an arrow between start and end with the arrow head at the end.
    Origin: https://www.reddit.com/r/pygame/comments/v3ofs9/draw_arrow_function/?rdt=40062

    Args:
        surface (pygame.Surface): The surface to draw on
        start (pygame.Vector2): Start position
        end (pygame.Vector2): End position
        color (pygame.Color): Color of the arrow
        body_width (int, optional): Defaults to 2.
        head_width (int, optional): Defaults to 4.
        head_height (float, optional): Defaults to 2.

    
    """
    arrow = start - end
    angle = arrow.angle_to(pygame.Vector2(0, -1))
    body_length = arrow.length() - head_height

    # Create the triangle head around the origin
    head_verts = [
        pygame.Vector2(0, head_height / 2),  # Center
        pygame.Vector2(head_width / 2, -head_height / 2),  # Bottomright
        pygame.Vector2(-head_width / 2, -head_height / 2),  # Bottomleft
    ]
    # Rotate and translate the head into place
    translation = pygame.Vector2(0, arrow.length() - (head_height / 2)).rotate(-angle)
    for i in range(len(head_verts)):
        head_verts[i].rotate_ip(-angle)
        head_verts[i] += translation
        head_verts[i] += start

    pygame.draw.polygon(surface, color, head_verts)

    # Stop weird shapes when the arrow is shorter than arrow head
    if arrow.length() >= head_height:
        # Calculate the body rect, rotate and translate into place
        body_verts = [
            pygame.Vector2(-body_width / 2, body_length / 2),  # Topleft
            pygame.Vector2(body_width / 2, body_length / 2),  # Topright
            pygame.Vector2(body_width / 2, -body_length / 2),  # Bottomright
            pygame.Vector2(-body_width / 2, -body_length / 2),  # Bottomleft
        ]
        translation = pygame.Vector2(0, body_length / 2).rotate(-angle)
        for i in range(len(body_verts)):
            body_verts[i].rotate_ip(-angle)
            body_verts[i] += translation
            body_verts[i] += start

        pygame.draw.polygon(surface, color, body_verts)

def draw_color_queue(queue, window, square_size, start_x, start_y, circle_radius):
    spacing = 10  # Spacing between circles
    for i, color_code in enumerate(queue):
        color = color_map[color_code]
        pygame.draw.circle(window, color, (start_x + i * (circle_radius * 2 + spacing), start_y), circle_radius)

def draw_instructions(window: pygame.Surface, square_size):
    # dimensions
    window_width = window.get_width()
    window_height = window.get_height()
    brim_height = square_size // 4
    top_height = square_size // 3
    brim_width = square_size - 20
    top_width = square_size - 35
    brim_padding_x = (square_size - brim_width) // 2
    top_padding_x = (square_size - top_width) // 2
    brim_y_offset = -10
    top_y_offset = -5
    brim_padding_y = (3 * square_size // 4) + brim_y_offset
    top_padding_y = (square_size - top_height) // 2 + top_y_offset

    # Draw the brim
    x_pos_brim = window_width - 5 * square_size + brim_padding_x
    y_pos_brim = 2 * square_size + brim_padding_y
    pygame.draw.rect(window, color_map[0], (x_pos_brim, y_pos_brim, brim_width, brim_height))

    # Draw the top
    x_pos_top = window_width - 4 * square_size + top_padding_x
    y_pos_top = 2 * square_size + top_padding_y
    pygame.draw.rect(window, color_map[1], (x_pos_top, y_pos_top, top_width, top_height))

    # Draw arrow
    x_pos_arrow = window_width - 3 * square_size + square_size // 8
    y_pos_arrow = 2 * square_size + square_size // 2
    arrow_length = 3 * square_size // 4
    body_width = square_size // 10
    arrow_height = square_size // 2
    head_width = arrow_length // 3
    draw_arrow(window, pygame.Vector2(x_pos_arrow, y_pos_arrow), pygame.Vector2(x_pos_arrow + arrow_length, y_pos_arrow), black, body_width, head_width, arrow_height)

    # Draw completed hat
    x_pos_brim_connected = window_width - 2 * square_size + brim_padding_x
    y_pos_brim_connected = 2 * square_size + brim_padding_y
    pygame.draw.rect(window, color_map[2], (x_pos_brim_connected, y_pos_brim_connected, brim_width, brim_height))
    x_pos_top_connected = window_width - 2 * square_size + top_padding_x
    y_pos_top_connected = 2 * square_size + top_padding_y
    pygame.draw.rect(window, color_map[0], (x_pos_top_connected, y_pos_top_connected, top_width, top_height))

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

    # Draw the outer frame with the correct offset for queue height
    pygame.draw.rect(window, frame_color, (0, queue_height, width * square_size + wall_thickness // 2 + 1, height * square_size + wall_thickness // 2 + 1), wall_thickness)

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
    draw_instructions(window, square_size)

def win(window) -> None:
    print("You won the game")
    win_image = pygame.image.load("img/win.svg")
    window.blit(win_image, win_image.get_rect(center = window.get_rect().center))

def game_over(window) -> None:
    print("You lost the game")
    game_over_image = pygame.image.load("img/game_over.svg")
    window.blit(game_over_image, game_over_image.get_rect(center = window.get_rect().center))
