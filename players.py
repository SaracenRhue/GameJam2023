import random

class Player:
    def __init__(self, color_count):
        self.x_pos = 0
        self.y_pos = 0
        self.color = 0 
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


    def move_up(self, world):
        if self.y_pos > 0 and world[self.y_pos - 1][self.x_pos][1] == self.color:
            self.y_pos -= 1
            print("Moved up")
        else: 
            print("Can't move up")

    def move_down(self, world):
        if self.y_pos < len(world) - 1 and world[self.y_pos][self.x_pos][1] == self.color:
            self.y_pos += 1
            print("Moved down")
        else:
            print("Can't move down")

    def move_left(self, world):
        if self.x_pos > 0 and world[self.y_pos][self.x_pos - 1][0] == self.color:
            self.x_pos -= 1
            print("Moved left")
        else:
            print("Can't move left")

    def move_right(self, world):
        if self.x_pos < len(world[0]) - 1 and world[self.y_pos][self.x_pos][0] == self.color:
            self.x_pos += 1
            print("Moved right")
        else:
            print("Can't move right")



def swap_colors(player0, player1):
    tmp = player0.get_color()
    player0.set_color(player1.get_color())
    player1.set_color(tmp)
    

# dummy_world = [[(1,0), (1,0)], [(1,2), (0,0)]]
# player = Player()
# player.move_down(dummy_world)
# print(player.get_position())
# player.move_right(dummy_world)
# print(player.get_position())
# player.move_up(dummy_world)
# print(player.get_position())