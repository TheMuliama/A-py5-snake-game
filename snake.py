import py5

WORLD_GRID_HEIGHT = 20
WORLD_GRID_WIDTH = 20
CELL_SIZE = 10

class player_class():
    def __init__(self):
        self.head_position_x = 4
        self.head_position_y = 5
        self.speed_x = 1
        self.speed_y = 0
        self.score = 0
    
    def update_position(self):
        self.head_position_x = self.head_position_x + self.speed_x
        self.head_position_y = self.head_position_y + self.speed_y

    def set_speed(self,new_speed_x, new_speed_y):
        self.speed_x = new_speed_x
        self.speed_y = new_speed_y

def clear_world_grid():
    return [[0 for j in range(WORLD_GRID_WIDTH)] for i in range(WORLD_GRID_HEIGHT)]

def draw_grid():
    for i in range(WORLD_GRID_WIDTH):
        for j in range(WORLD_GRID_HEIGHT):
            if world_grid[j][i] == 1:
                py5.square(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE)

def setup():
    global world_grid, player
    py5.size(WORLD_GRID_WIDTH * CELL_SIZE, WORLD_GRID_HEIGHT * CELL_SIZE)
    py5.background(0)
    py5.no_stroke()
    player = player_class()
    world_grid = clear_world_grid()

def draw():
    global player, world_grid, tmp

    py5.background(0)
    world_grid = clear_world_grid()
    player.set_speed(player.speed_x * -1, 0)
    player.update_position()
    world_grid[player.head_position_x][player.head_position_y] = 1
    
    draw_grid()

py5.run_sketch()