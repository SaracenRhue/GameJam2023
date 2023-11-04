import random
import typing

class Queue():
    def __init__(self, color_count, length=3):
        self.color_count = color_count
        self.length = length
        self.queue = random.sample(range(color_count), color_count)

    def get_queue(self):
        return self.queue
    
    def update_queue(self, world, players):
        players_copy = []
        for player in players:
            player_copy = Player()
            player_copy.x_pos = player.x_pos
            player_copy.y_pos = player.y_pos
            player_copy.color = player.color
            players_copy.append(player_copy)
        queue_copy = Queue(self.color_count, self.length)
        queue_copy.queue = self.queue
        while len(self.queue) < self.length:
            possible_next_colors_for_valid_paths = self.__possible_next_colors_for_valid_paths(world, players_copy, queue_copy)
            if len(possible_next_colors_for_valid_paths) == 0:
                print("You chose a wrong path and you are stuck")
                return
            next_color_index = random.randrange(len(possible_next_colors_for_valid_paths))
            next_color = possible_next_colors_for_valid_paths[next_color_index]
            self.queue.append(next_color)
        print(f"Updated queue to {self.queue}")
        
    def __possible_next_colors_for_valid_paths(self, world, players, queue) -> typing.Tuple[int]:
        possible_next_colors = set()

        current_colors = set(player.color for player in players)
        if None in current_colors:
            player_with_none = next(filter(lambda player: player.color is None, players))
            if player_with_none.y_pos > 0:
                top_wall_color = world[player_with_none.y_pos - 1][player_with_none.x_pos][1]
                possible_next_colors.add(top_wall_color)
            if player_with_none.y_pos < len(world) - 1:
                bottom_wall_color = world[player_with_none.y_pos][player_with_none.x_pos][1]
                possible_next_colors.add(bottom_wall_color)
            if player_with_none.x_pos > 0:
                left_wall_color = world[player_with_none.y_pos][player_with_none.x_pos - 1][0]
                possible_next_colors.add(left_wall_color)
            if player_with_none.x_pos < len(world[0]) - 1:
                right_wall_color = world[player_with_none.y_pos][player_with_none.x_pos][0]
                possible_next_colors.add(right_wall_color)
            return tuple(possible_next_colors)

        for player in players:
            current_position = (player.x_pos, player.y_pos)
            for color in current_colors:
                player.color = color
                player.move_up(world, queue)
                if player.x_pos != current_position[0] or player.y_pos != current_position[1]:
                    queue_copy = Queue(self.color_count, self.length)
                    queue_copy.queue = queue.get_queue()[1:]
                    possible_next_colors.update(self.__possible_next_colors_for_valid_paths(world, players, queue_copy))
                    player.x_pos, player.y_pos = current_position
                player.move_down(world, queue)
                if player.x_pos != current_position[0] or player.y_pos != current_position[1]:
                    queue_copy = Queue(self.color_count, self.length)
                    queue_copy.queue = queue.get_queue()[1:]
                    possible_next_colors.update(self.__possible_next_colors_for_valid_paths(world, players, queue_copy))
                    player.x_pos, player.y_pos = current_position
                player.move_left(world, queue)
                if player.x_pos != current_position[0] or player.y_pos != current_position[1]:
                    queue_copy = Queue(self.color_count, self.length)
                    queue_copy.queue = queue.get_queue()[1:]
                    possible_next_colors.update(self.__possible_next_colors_for_valid_paths(world, players, queue_copy))
                    player.x_pos, player.y_pos = current_position
                player.move_right(world, queue)
                if player.x_pos != current_position[0] or player.y_pos != current_position[1]:
                    queue_copy = Queue(self.color_count, self.length)
                    queue_copy.queue = queue.get_queue()[1:]
                    possible_next_colors.update(self.__possible_next_colors_for_valid_paths(world, players, queue_copy))
                    player.x_pos, player.y_pos = current_position

        return tuple(possible_next_colors)

class Player:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.color = 0 

    def get_position(self):
        return (self.x_pos, self.y_pos)
    
    def set_position(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def update_color(self, queue):
        if len(queue.get_queue()) > 0:
            self.color = queue.get_queue()[0]
        else:
            self.color = None
        print(f"Updated player color to {self.color}")

    def move_up(self, world, queue) -> bool:
        if self.y_pos > 0:
            above_bottom_wall_color = world[self.y_pos - 1][self.x_pos][1]
            print(f"Trying to move up. Above bottom wall color: {above_bottom_wall_color}, Player color: {self.color}")
            if above_bottom_wall_color == self.color:
                self.y_pos -= 1
                self.update_color(queue)
                print("Moved up")
                return True
            else:
                print("Can't move up - wall color does not match player color")
        else:
            print("Can't move up - at the top edge")
        return False

    def move_down(self, world, queue) -> bool:
        if self.y_pos < len(world) - 1:
            current_bottom_wall_color = world[self.y_pos][self.x_pos][1]
            print(f"Trying to move down. Current bottom wall color: {current_bottom_wall_color}, Player color: {self.color}")
            if current_bottom_wall_color == self.color:
                self.y_pos += 1
                self.update_color(queue)
                print("Moved down")
                return True
            else:
                print("Can't move down - wall color does not match player color")
        else:
            print("Can't move down - at the bottom edge")
        return False

    def move_left(self, world, queue) -> bool:
        if self.x_pos > 0:
            left_right_wall_color = world[self.y_pos][self.x_pos - 1][0]
            print(f"Trying to move left. Left right wall color: {left_right_wall_color}, Player color: {self.color}")
            if left_right_wall_color == self.color:
                self.x_pos -= 1
                self.update_color(queue)
                print("Moved left")
                return True
            else:
                print("Can't move left - wall color does not match player color")
        else:
            print("Can't move left - at the left edge")
        return False

    def move_right(self, world, queue) -> bool:
        if self.x_pos < len(world[0]) - 1:
            current_right_wall_color = world[self.y_pos][self.x_pos][0]
            print(f"Trying to move right. Current right wall color: {current_right_wall_color}, Player color: {self.color}")
            if current_right_wall_color == self.color:
                self.x_pos += 1
                self.update_color(queue)
                print("Moved right")
                return True
            else:
                print("Can't move right - wall color does not match player color")
        else:
            print("Can't move right - at the right edge")
        return False



def swap_colors(player0, player1):
    tmp = player0.get_color()
    player0.set_color(player1.get_color())
    player1.set_color(tmp)