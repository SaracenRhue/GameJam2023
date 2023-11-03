import random

def get_layout(width: int, height: int, color_count: int) -> list: 
    """Returns a list of 2-tuples representing right and bottom wall colors by integers"""
    print(f"Getting layout for a world of size {width}x{height} with {color_count} colors")

    result = []
    for i in range(height):
        row = []
        for i in range(width):
            right_wall = random.randrange(color_count)
            bottom_wall = random.randrange(color_count)
            row.append((right_wall, bottom_wall))
        result.append(row)

    return result