import random

class Queue():
    def __init__(self, color_count, length=3):
        self.color_count = color_count
        self.length = length
        self.queue = random.sample(range(color_count), color_count)

    def get_queue(self):
        return self.queue
    
    def update_queue(self):
        self.queue.pop(0)
        self.queue.append(random.randrange(self.color_count))
        print(f"Updated queue to {self.queue}")


class Player:
    def __init__(self, world, color_count):
        self.x_pos = 0
        self.y_pos = 0
        self.color = 0 
        self.color_count = color_count
        self.color_queue = random.sample(range(color_count), color_count)

    def get_position(self):
        return (self.x_pos, self.y_pos)
    
    def set_position(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def update_color(self, Queue):
        # self.color = Queue.queue[0]
        self.color_queue.pop(0)
        self.color_queue.append(random.randrange(self.color_count))
        print(f"Updated player color to {self.color} and color queue to {self.color_queue}")

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