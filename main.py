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
    width, height = random.randrange(5, 15), random.randrange(5, 15)
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

    window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN) 

    
# Initialize the game
restart_game()

# Adjust window size based on grid dimensions and square size
window_height = (len(world) + 1) * square_size  # +1 to add space for the queue
window_width = len(world[0]) * square_size

window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN) 
pygame.display.set_caption('RGB')

running = True
dark_mode = False
won_or_game_over = False

while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:  # If the close button is clicked
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_r or event.key == K_p:
                won_or_game_over = False
                restart_game()  # Restarts the game when 'r' is pressed
            elif event.key == K_q or event.key == K_ESCAPE:
                running = False

    if not won_or_game_over:
        # Handle events
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_c or event.key == K_u:
                    swap_colors(players[0], players[1])
                elif event.key == K_SPACE or event.key == K_h:
                    current_player = 1 - current_player
                elif event.key == K_w:
                    if players[current_player].move_up(world, queue):
                        queue.get_queue().pop(0)
                        queue.update_queue(world, players)
                elif event.key == K_s:
                    if players[current_player].move_down(world, queue):
                        queue.get_queue().pop(0)
                        queue.update_queue(world, players)
                elif event.key == K_a:
                    if players[current_player].move_left(world, queue):
                        queue.get_queue().pop(0)
                        queue.update_queue(world, players)
                elif event.key == K_d:
                    if players[current_player].move_right(world, queue):
                        queue.get_queue().pop(0)
                        queue.update_queue(world, players)
                # elif event.key == K_:
                

        # Draw the world and the player
        ui.draw_world(queue, world, players, current_player, window, square_size)

        # Check for win or game over
        if players[0].x_pos == players[1].x_pos and players[0].y_pos == players[1].y_pos:
            ui.win(window)
            won_or_game_over = True
        elif len(queue.get_queue()) < queue.length:
            ui.game_over(window)
            won_or_game_over = True

        # Update the display
        pygame.display.flip()

    # Cap the framerate
    clock.tick(fps)

pygame.quit()
