import pygame



dummy_list=[[(2, 3), (1, 1), (3, 3), (2, 2), (0, 0)],
[(2, 1), (0, 0), (3, 2), (0, 2), (3, 2)],
[(3, 0), (1, 0), (3, 0), (1, 1), (1, 0)],
[(3, 1), (0, 2), (0, 2), (1, 3), (3, 2)],
[(2, 1), (3, 2), (0, 2), (2, 0), (0, 0)]
]


# Define colors
colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]  # [red, blue, green, yellow]

# Window size
window_width = 400
window_height = 400

# Grid size
rows = len(dummy_list)
columns = len(dummy_list[0])
cell_width = window_width // columns
cell_height = window_height // rows

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))

# Loop to draw the grid
for row in range(rows):
    for column in range(columns):
        right_border_color, bottom_border_color = dummy_list[row][column]
        x = column * cell_width
        y = row * cell_height
        pygame.draw.rect(screen, colors[right_border_color], (x, y, cell_width, cell_height))
        pygame.draw.line(screen, colors[bottom_border_color], (x, y + cell_height), (x + cell_width, y + cell_height))

# Update the screen
pygame.display.flip()

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

