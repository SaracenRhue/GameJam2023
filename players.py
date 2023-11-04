import random
import typing

class Player:
    def __init__(self, world_layout, color_count, color_queue_length = 3):
        self.x_pos = 0
        self.y_pos = 0
        self.color = 0
        self.world_layout = world_layout
        self.color_count = color_count
        self.color_queue_length = color_queue_length
        self.color_queue = []
        self.update_color_queue()

    def get_position(self):
        return (self.x_pos, self.y_pos)
    
    def set_position(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def update_color(self):
        self.color = self.color_queue[0]
        self.color_queue.pop(0)
        self.update_color_queue()
        print(f"Updated player color to {self.color} with color queue {self.color_queue}")

    def update_color_queue(self) -> None:
        while len(self.color_queue) < self.color_queue_length:
            possible_next_colors_for_valid_paths = self.__possible_next_colors_for_valid_paths((self.x_pos, self.y_pos), -1)
            if len(possible_next_colors_for_valid_paths) == 0:
                print("You chose a wrong path and you are stuck")
                return
            next_color_index = random.randrange(len(possible_next_colors_for_valid_paths))
            next_color = possible_next_colors_for_valid_paths[next_color_index]
            self.color_queue.append(next_color)

    def __possible_next_colors_for_valid_paths(self, current_position: typing.Tuple[int, int], color_queue_index: int) -> typing.Tuple[int]:
        possible_next_colors = set()
        top_wall_color = None
        bottom_wall_color = None
        left_wall_color = None
        right_wall_color = None

        if current_position[1] > 0:
            top_wall_color = self.world_layout[current_position[1] - 1][current_position[0]][1]
        if current_position[1] < len(self.world_layout) - 1:
            bottom_wall_color = self.world_layout[current_position[1]][current_position[0]][1]
        if current_position[0] > 0:
            left_wall_color = self.world_layout[current_position[1]][current_position[0] - 1][0]
        if current_position[0] < len(self.world_layout[0]) - 1:
            right_wall_color = self.world_layout[current_position[1]][current_position[0]][0]

        if color_queue_index >= len(self.color_queue):
            possible_next_colors.add(top_wall_color)
            possible_next_colors.add(bottom_wall_color)
            possible_next_colors.add(left_wall_color)
            possible_next_colors.add(right_wall_color)
            possible_next_colors.discard(None)
            return tuple(possible_next_colors)
        
        current_color = self.color
        if color_queue_index >= 0:
            current_color = self.color_queue[color_queue_index]

        if top_wall_color == current_color:
            possible_next_colors.update(self.__possible_next_colors_for_valid_paths((current_position[0], current_position[1] - 1), color_queue_index + 1))
        if bottom_wall_color == current_color:
            possible_next_colors.update(self.__possible_next_colors_for_valid_paths((current_position[0], current_position[1] + 1), color_queue_index + 1))
        if left_wall_color == current_color:
            possible_next_colors.update(self.__possible_next_colors_for_valid_paths((current_position[0] - 1, current_position[1]), color_queue_index + 1))
        if right_wall_color == current_color:
            possible_next_colors.update(self.__possible_next_colors_for_valid_paths((current_position[0] + 1, current_position[1]), color_queue_index + 1))

        return tuple(possible_next_colors)

    def move_up(self, world):
        if self.y_pos > 0:
            above_bottom_wall_color = world[self.y_pos - 1][self.x_pos][1]
            print(f"Trying to move up. Above bottom wall color: {above_bottom_wall_color}, Player color: {self.color}")
            if above_bottom_wall_color == self.color:
                self.y_pos -= 1
                self.update_color()
                print("Moved up")
            else:
                print("Can't move up - wall color does not match player color")
        else:
            print("Can't move up - at the top edge")

    def move_down(self, world):
        if self.y_pos < len(world) - 1:
            current_bottom_wall_color = world[self.y_pos][self.x_pos][1]
            print(f"Trying to move down. Current bottom wall color: {current_bottom_wall_color}, Player color: {self.color}")
            if current_bottom_wall_color == self.color:
                self.y_pos += 1
                self.update_color()
                print("Moved down")
            else:
                print("Can't move down - wall color does not match player color")
        else:
            print("Can't move down - at the bottom edge")

    def move_left(self, world):
        if self.x_pos > 0:
            left_right_wall_color = world[self.y_pos][self.x_pos - 1][0]
            print(f"Trying to move left. Left right wall color: {left_right_wall_color}, Player color: {self.color}")
            if left_right_wall_color == self.color:
                self.x_pos -= 1
                self.update_color()
                print("Moved left")
            else:
                print("Can't move left - wall color does not match player color")
        else:
            print("Can't move left - at the left edge")

    def move_right(self, world):
        if self.x_pos < len(world[0]) - 1:
            current_right_wall_color = world[self.y_pos][self.x_pos][0]
            print(f"Trying to move right. Current right wall color: {current_right_wall_color}, Player color: {self.color}")
            if current_right_wall_color == self.color:
                self.x_pos += 1
                self.update_color()
                print("Moved right")
            else:
                print("Can't move right - wall color does not match player color")
        else:
            print("Can't move right - at the right edge")



def swap_colors(player0, player1):
    tmp = player0.get_color()
    player0.set_color(player1.get_color())
    player1.set_color(tmp)