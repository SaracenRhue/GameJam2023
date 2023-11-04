import pygame
from pygame.locals import *
from players import Player
import world as layout
import ui

pygame.init()

fps = 25
width, height = 4, 4  # Grid dimensions
square_size = 50  # Size of each square in pixels
color_count = 3  

# Adjust window size based on grid dimensions and square size
window_width = width * square_size
window_height = height * square_size
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pygame Player Movement')

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Function to initialize/restart the game
def restart_game():
    global player, world
    player = Player(color_count)
    world = layout.get_layout(width, height, color_count)

# Initialize the game
restart_game()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Quit if 'Q' is pressed
    if keys[K_q]:
        running = False
    
    # Restart if 'R' is pressed
    if keys[K_r]:
        restart_game()

    # Move the player with WASD
    if keys[K_w]:
        player.move_up(world)
    if keys[K_s]:
        player.move_down(world)
    if keys[K_a]:
        player.move_left(world)
    if keys[K_d]:
        player.move_right(world)

    # Draw the world and the player
    ui.draw_world(world, player, window, square_size)

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(fps)

pygame.quit()
