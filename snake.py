import py5
import random

WORLD_GRID_HEIGHT = 30
WORLD_GRID_WIDTH = 30
CELL_SIZE = 10
GAME_COOLDOWN = 8

apple_position = [0,0]

class player_class():
    def __init__(self):
        self.head_position_x = WORLD_GRID_WIDTH//2
        self.head_position_y = WORLD_GRID_HEIGHT//2
        self.body = [[self.head_position_x-1, self.head_position_y], [self.head_position_x-2, self.head_position_y], [self.head_position_x-3, self.head_position_y]]
        self.speed_x = 1
        self.speed_y = 0
        self.score = 0
    
    def update_position(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i] = self.body[i-1]
        self.body[0] = [self.head_position_x, self.head_position_y]
        self.head_position_x = self.head_position_x + self.speed_x
        self.head_position_y = self.head_position_y + self.speed_y

    def set_speed(self,new_speed_x, new_speed_y):
        self.speed_x = new_speed_x
        self.speed_y = new_speed_y
    
    def is_self_colliding(self):
        for body_part in self.body:
            if body_part == [self.head_position_x, self.head_position_y]:
                return True
        return False

def clear_world_grid():
    return [[0 for j in range(WORLD_GRID_WIDTH)] for i in range(WORLD_GRID_HEIGHT)]

def draw_grid():
    py5.fill(250,100,100)
    py5.square(apple_position[0]*CELL_SIZE, apple_position[1]*CELL_SIZE, CELL_SIZE)
    py5.fill(255)
    for i in range(WORLD_GRID_WIDTH):
        for j in range(WORLD_GRID_HEIGHT):
            if world_grid[j][i] == 1:
                py5.square(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE)
    

def update_world():
    global player, world_grid, current_cooldown, apple_position
    world_grid = clear_world_grid()

    if [player.head_position_x, player.head_position_y] == apple_position:
        player.body = player.body + player.body[-1]
        apple_position = new_apple_position()

    player.update_position()
    
    if border_collision() == True:
        print("The player touched the border!!! \n")

    if player.is_self_colliding():
        print("The player bumped into himself!!! \n")

    for body_part in player.body:
        world_grid[body_part[1]][body_part[0]] = 1
    
    world_grid[player.head_position_y][player.head_position_x] = 1
    current_cooldown = GAME_COOLDOWN

def key_pressed():
    global player, world_grid

    if py5.key_code == py5.UP and player.speed_y != 1:
        player.set_speed(0,-1)

    if py5.key_code == py5.DOWN and player.speed_y != -1:
        player.set_speed(0,1)

    if py5.key_code == py5.LEFT and player.speed_x != 1:
        player.set_speed(-1,0)    

    if py5.key_code == py5.RIGHT and player.speed_x != -1:
        player.set_speed(1,0)

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

def new_apple_position():
    global world_grid, player
    apple_position = [random.randint(0,WORLD_GRID_WIDTH-1), random.randint(0,WORLD_GRID_HEIGHT-1)]

    for body_part in player.body:
        
        if apple_position == [body_part[0], body_part[1]]:
            apple_position = new_apple_position()
        if apple_position == [player.head_position_x, player.head_position_y]:
            apple_position = new_apple_position()
    print(f"new apple position: {apple_position}")
    return apple_position

def setup():
    global world_grid, player, current_cooldown, apple_position
    py5.size(WORLD_GRID_WIDTH * CELL_SIZE, WORLD_GRID_HEIGHT * CELL_SIZE)
    py5.background(0)
    py5.no_stroke()
    player = player_class()
    world_grid = clear_world_grid()
    apple_position = new_apple_position()
    current_cooldown = GAME_COOLDOWN

def draw():
    global player, world_grid, current_cooldown, apple_position

    py5.background(0)

    current_cooldown = current_cooldown - 1
    if current_cooldown < 0:
        update_world()
        
    
    
    
    draw_grid()

py5.run_sketch()