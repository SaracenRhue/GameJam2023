import random
import typing

def get_layout(width: int, height: int, color_count: int, initial_color: int = 0) -> typing.List[typing.List[typing.Tuple[int, int]]]:
    """Returns a list of lists of 2-tuples representing right and bottom wall colors by integers"""
    return _get_random_layout(width, height, color_count, initial_color)

def _get_random_layout(width: int, height: int, color_count: int, initial_color: int) -> typing.List[typing.List[typing.Tuple[int, int]]]:
    print(f"Getting layout for a world of size {width}x{height} with {color_count} colors")
    result = []
    for i in range(height):
        row = []
        for i in range(width):
            right_wall = random.randrange(color_count)
            bottom_wall = random.randrange(color_count)
            row.append((right_wall, bottom_wall))
        result.append(row)

    if not initial_color in result[0][0]:
        # change right or bottom wall to match initial_color to prevent an impossible level
        index = random.randrange(2)
        first_cell_tuple_as_list = list(result[0][0])
        first_cell_tuple_as_list[index] = initial_color
        result[0][0] = tuple(first_cell_tuple_as_list)

    return result
