import pygame
import random
pygame.mixer.init()
sound_effect1 = pygame.mixer.Sound("burst-decent.wav")
sound_effect2 = pygame.mixer.Sound("game-over.game-over.wav")

# Define constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30
WINDOW_WIDTH = GRID_WIDTH * BLOCK_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define tetrominos
I_TETROMINO = [[1, 1, 1, 1]]
J_TETROMINO = [[2, 0, 0], [2, 2, 2]]
L_TETROMINO = [[0, 0, 3], [3, 3, 3]]
O_TETROMINO = [[4, 4], [4, 4]]
S_TETROMINO = [[0, 5, 5], [5, 5, 0]]
T_TETROMINO = [[6, 6, 6], [0, 6, 0]]
Z_TETROMINO = [[7, 7, 0], [0, 7, 7]]
TETROMINOS = [I_TETROMINO, J_TETROMINO, L_TETROMINO, O_TETROMINO, S_TETROMINO, T_TETROMINO, Z_TETROMINO]
TETROMINO_COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]

# Define game functions
def draw_block(x, y, value):
    color = TETROMINO_COLORS[value - 1]
    block_rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, color, block_rect)

def new_tetromino():
    tetromino = random.choice(TETROMINOS)
    color = random.choice(TETROMINO_COLORS)
    x = (GRID_WIDTH - len(tetromino[0])) // 2
    y = 0
    return tetromino, color, x, y

def check_collision(grid, tetromino, x, y):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] != 0:
                if x + j < 0 or x + j >= GRID_WIDTH or y + i >= GRID_HEIGHT or grid[y + i][x + j] != 0:
                    return True
    return False

def update_grid(grid, tetromino, x, y):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] != 0:
                grid[y + i][x + j] = tetromino[i][j]

def remove_row(grid, row):
    del grid[row]
    grid.insert(0, [0] * GRID_WIDTH)

def remove_rows(grid):
    rows_removed = 0
    row = GRID_HEIGHT - 1
    while row >= 0:
        if 0 not in grid[row]:
            remove_row(grid, row)
            rows_removed += 1
        else:
            row -= 1
    return rows_removed

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('TetraPY')

import pygame
import random

# Define constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30
WINDOW_WIDTH = GRID_WIDTH * BLOCK_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define tetrominos
I_TETROMINO = [[1, 1, 1, 1]]
J_TETROMINO = [[2, 0, 0], [2, 2, 2]]
L_TETROMINO = [[0, 0, 3], [3, 3, 3]]
O_TETROMINO = [[4, 4], [4, 4]]
S_TETROMINO = [[0, 5, 5], [5, 5, 0]]
T_TETROMINO = [[6, 6, 6], [0, 6, 0]]
Z_TETROMINO = [[7, 7, 0], [0, 7, 7]]
TETROMINOS = [I_TETROMINO, J_TETROMINO, L_TETROMINO, O_TETROMINO, S_TETROMINO, T_TETROMINO, Z_TETROMINO]
TETROMINO_COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]

# Define game functions
def draw_block(x, y, value):
    color = TETROMINO_COLORS[value - 1]
    block_rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(screen, color, block_rect)

def new_tetromino():
    tetromino = random.choice(TETROMINOS)
    color = random.choice(TETROMINO_COLORS)
    x = (GRID_WIDTH - len(tetromino[0])) // 2
    y = 0
    return tetromino, color, x, y

def check_collision(grid, tetromino, x, y):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] != 0:
                if x + j < 0 or x + j >= GRID_WIDTH or y + i >= GRID_HEIGHT or grid[y + i][x + j] != 0:
                    return True
    return False

def update_grid(grid, tetromino, x, y):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] != 0:
                grid[y + i][x + j] = tetromino[i][j]

def remove_row(grid, row):
    del grid[row]
    grid.insert(0, [0] * GRID_WIDTH)
  sound_effect2.play()
def remove_rows(grid):
    rows_removed = 0
    row = GRID_HEIGHT - 1
    while row >= 0:
        if 0 not in grid[row]:
            remove_row(grid, row)
            rows_removed += 1
        else:
            row -= 1
    return rows_removed

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('TetraPY')

# Initialize the game state
clock = pygame.time.Clock()
game_over = False
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
fall_rate = 1
score = 0

# Create the first tetromino
tetromino, color, x, y = new_tetromino()

# Start the game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not check_collision(grid, tetromino, x - 1, y):
                    x -= 1
            elif event.key == pygame.K_RIGHT:
                if not check_collision(grid, tetromino, x + 1, y):
                    x += 1
            elif event.key == pygame.K_DOWN:
                if not check_collision(grid, tetromino, x, y + 1):
                    y += 1
                else:
                    update_grid(grid, tetromino, x, y)
                    rows_removed = remove_rows(grid)
                    score += rows_removed ** 2
                    tetromino, color, x, y = new_tetromino()
                    if check_collision(grid, tetromino, x, y):
                        game_over = True
                    fall_rate = 1
            elif event.key == pygame.K_UP:
                rotated_tetromino = [[tetromino[j][i] for j in range(len(tetromino))] for i in range(len(tetromino[0]) - 1, -1, -1)]
                if not check_collision(grid, rotated_tetromino, x, y):
                    tetromino = rotated_tetromino

    # Handle falling tetromino
    fall_delay = 30 / (fall_rate ** 0.5)
    if pygame.time.get_ticks() % int(fall_delay) == 0:
        if not check_collision(grid, tetromino, x, y + 1):
            y += 1
        else:
            update_grid(grid, tetromino, x, y)
            rows_removed = remove_rows(grid)
            score += rows_removed ** 2
            tetromino, color, x, y = new_tetromino()
            if check_collision(grid, tetromino, x, y):
                game_over = True
            fall_rate = max(1, fall_rate + rows_removed // 2)

    # Draw the screen
    screen.fill(BLACK)
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if grid[i][j] != 0:
                draw_block(j, i, grid[i][j])
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] != 0:
                draw_block(x + j, y + i, tetromino[i][j])

    pygame.display.set_caption('TetraPY - Score: {}'.format(score))
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

# Clean up
pygame.quit()

# Initialize the game state
clock = pygame.time.Clock()
game_over = False
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
fall_rate = 1
score = 0

# Create the first tetromino
tetromino, color, x, y = new_tetromino()

# Start the game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not check_collision(grid, tetromino, x - 1, y):
                    x -= 1
            elif event.key == pygame.K_RIGHT:
                if not check_collision(grid, tetromino, x + 1, y):
                    x += 1
            elif event.key == pygame.K_DOWN:
                if not check_collision(grid, tetromino, x, y + 1):
                    y += 1
                else:
                    update_grid(grid, tetromino, x, y)
                    rows_removed = remove_rows(grid)
                    score += rows_removed ** 2
                    tetromino, color, x, y = new_tetromino()
                    if check_collision(grid, tetromino, x, y):
                        game_over = True
                    fall_rate = 1
            elif event.key == pygame.K_UP:
                rotated_tetromino = [[tetromino[j][i] for j in range(len(tetromino))] for i in range(len(tetromino[0]) - 1, -1, -1)]
                if not check_collision(grid, rotated_tetromino, x, y):
                    tetromino = rotated_tetromino

    # Handle falling tetromino
    fall_delay = 30 / (fall_rate ** 0.5)
    if pygame.time.get_ticks() % int(fall_delay) == 0:
        if not check_collision(grid, tetromino, x, y + 1):
            y += 1
        else:
            update_grid(grid, tetromino, x, y)
            rows_removed = remove_rows(grid)
            score += rows_removed ** 2
            tetromino, color, x, y = new_tetromino()
            if check_collision(grid, tetromino, x, y):
                game_over = True
              sound_effect1.play()
            fall_rate = max(1, fall_rate + rows_removed // 2)

    # Draw the screen
    screen.fill(BLACK)
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if grid[i][j] != 0:
                draw_block(j, i, grid[i][j])
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] != 0:
                draw_block(x + j, y + i, tetromino[i][j])
    pygame.display.set_caption('TetraPY - Score: {}'.format(score))
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

# Clean up
pygame.quit()