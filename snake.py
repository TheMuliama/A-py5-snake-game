import py5

WORLD_GRID_HEIGHT = 20
WORLD_GRID_WIDTH = 30
CELL_SIZE = 15
GAME_COOLDOWN = 20

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

def update_world():
    global player, world_grid, current_cooldown
    world_grid = clear_world_grid()
    player.update_position()
    if border_collision() == True:
        print("The player touched the border!!! \n")
    world_grid[player.head_position_y][player.head_position_x] = 1
    current_cooldown = GAME_COOLDOWN

def key_pressed():
    global player, world_grid

    if py5.key_code == py5.UP:
        player.set_speed(0,-1)

    if py5.key_code == py5.DOWN:
        player.set_speed(0,1)

    if py5.key_code == py5.RIGHT:
        player.set_speed(1,0)

    if py5.key_code == py5.LEFT:
        player.set_speed(-1,0)

def border_collision():
    global player
    is_colliding = False
    if player.head_position_x > WORLD_GRID_WIDTH - 1:
        player.head_position_x = WORLD_GRID_WIDTH - 1
        is_colliding = True

    if player.head_position_x < 0:
        player.head_position_x = 0
        is_colliding = True
    
    if player.head_position_y > WORLD_GRID_HEIGHT - 1:
        player.head_position_y = WORLD_GRID_HEIGHT - 1
        is_colliding = True
        
    if player.head_position_y < 0:
        player.head_position_y = 0
        is_colliding = True
    
    return is_colliding
    


def setup():
    global world_grid, player, current_cooldown
    py5.size(WORLD_GRID_WIDTH * CELL_SIZE, WORLD_GRID_HEIGHT * CELL_SIZE)
    py5.background(0)
    py5.no_stroke()
    player = player_class()
    world_grid = clear_world_grid()
    current_cooldown = GAME_COOLDOWN

def draw():
    global player, world_grid, current_cooldown

    py5.background(0)

    current_cooldown = current_cooldown - 1
    if current_cooldown < 0:
        update_world()
    
    
    draw_grid()

py5.run_sketch()