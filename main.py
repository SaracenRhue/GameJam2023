import pygame
from pygame.locals import *
from players import Player
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
    global player, world, width, height
    width, height = random.randrange(5, 20), random.randrange(5, 20)
    world = layout.get_layout(width, height, color_count)
    player = Player(world, color_count)
    
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
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            # Use an if-elif block to handle a single key press event
            if event.key == K_w:
                player.move_up(world)
            elif event.key == K_s:
                player.move_down(world)
            elif event.key == K_a:
                player.move_left(world)
            elif event.key == K_d:
                player.move_right(world)

    # Draw the world and the player
    ui.draw_world(world, player, window, square_size)

    # Update the display
    pygame.display.flip()

    # Cap the framerate
    clock.tick(fps)

pygame.quit()
