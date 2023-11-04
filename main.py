import pygame
from pygame.locals import *
from players import Player, Queue, swap_colors
import world as layout
import random
import ui

pygame.init()

fps = 25
square_size = 50  # Size of each square in pixels
color_count = 3  

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Function to initialize/restart the game
def restart_game():
    global players, current_player, world, width, height, window, queue
    width, height = random.randrange(5, 20), random.randrange(5, 20)
    world = layout.get_layout(width, height, color_count)
    queue = Queue(color_count)
    player0 = Player()
    player0.set_position(0, 0)
    player1 = Player()
    player1.set_position(width - 1, height - 1)
    players = [player0, player1]
    current_player = 0
    
    # Adjust window size based on grid dimensions and square size
    window_height = (height + 1) * square_size  # +1 to add space for the queue
    window_width = width * square_size

    window = pygame.display.set_mode((window_width, window_height)) 
    
# Initialize the game
restart_game()

# Adjust window size based on grid dimensions and square size
window_height = (len(world) + 1) * square_size  # +1 to add space for the queue
window_width = len(world[0]) * square_size

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pygame Player Movement')

running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:  # If the close button is clicked
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_r:
                restart_game()  # Restarts the game when 'r' is pressed
            elif event.key == K_c:
                swap_colors(players[0], players[1])
            elif event.key == K_SPACE:
                current_player = 1 - current_player
            elif event.key == K_w:
                players[current_player].move_up(world, queue)
            elif event.key == K_s:
                players[current_player].move_down(world, queue)
            elif event.key == K_a:
                players[current_player].move_left(world, queue)
            elif event.key == K_d:
                players[current_player].move_right(world, queue)
            elif event.key == K_q:
                running = False


    # Draw the world and the player
    ui.draw_world(queue, world, players, current_player, window, square_size)

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(fps)

pygame.quit()
