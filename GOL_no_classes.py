import random
import sys
from time import sleep
import pygame

"""
this is a conways game of life implementation, no classes or dictionaries this time.
p - Pause/Unpause
c - change colors
q - quit
"""
BoardX = 120
BoardY = 80
dead_color = random.choice(
    [(0, 100, 102), (6, 90, 96), (11, 82, 91), (20, 69, 82), (27, 58, 75), (33, 47, 69), (39, 38, 64), (62, 31, 71)]
)
live_color = random.choice(
    [(255, 0, 0), (255, 135, 0), (255, 211, 0), (222, 255, 10), (161, 255, 10), (10, 255, 153), (10, 239, 255),
     (20, 125, 245), (88, 10, 255), (190, 10, 255)]
)


def update(surface, board):
    """
    updates the pygame surface with the new states of cells
    :param surface: pygame surface
    :param board: the matrix of cells
    :return: None
    """
    for row in board:
        for cell in row:
            if cell[3] == 'live':
                col = live_color
                pygame.draw.rect(surface, col, (cell[0][0] * 8, cell[0][1] * 8, 8 - 1, 8 - 1))
                cell[2] = cell[3]
            else:
                col = dead_color
                pygame.draw.rect(surface, col, (cell[0][0] * 8, cell[0][1] * 8, 8 - 1, 8 - 1))
                cell[2] = cell[3]


def compute_next(board, cell):
    """
    calculates the next state of each cell of the board with the game logic
    :param board: matrix of cells
    :param cell: specific cell
    :return: None
    """
    neighbor_stats = []
    for neighbor in cell[1]:
        neighbor_stats.append(board[neighbor[0]][neighbor[1]][2])
    count = neighbor_stats.count('live')
    # game logic:
    if cell[2] == 'live':
        if count <= 1 or count > 3:
            cell[3] = 'dead'
        neighbor_stats = []
    else:
        if count == 3:
            cell[3] = 'live'
        neighbor_stats = []


locations = [(x, y) for x in range(BoardX) for y in range(BoardY)]  # tuples of (x,y) of each cell on the game board
board = [list() for row in range(BoardX)]  # init the game board matrix
for loc in locations:  # fill the board matrix with cells, computing the neighbor locations of each cell, random state
    neighbors = [(x, y) for x in range(loc[0] - 1, loc[0] + 2) for y in
                 range(loc[1] - 1, loc[1] + 2) if
                 (x, y) != loc and 0 <= x < BoardX and 0 <= y < BoardY]
    state = random.choice(['live', 'dead'])
    next_state = None
    board[loc[0]].append([loc, neighbors, state, next_state])

#
paused = False
if __name__ == '__main__':
    pygame.init()
    Surface = pygame.display.set_mode((BoardX * 8, BoardY * 8))
    pygame.display.set_caption('THE GAME OF LIFE - no classes or dicts')
    for row in board:
        for cell in row:
            pygame.draw.rect(Surface, live_color,
                             (cell[0][0] * 8, cell[0][1] * 8, 8 - 1, 8 - 1))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pausing/Unpausing
                    paused = not paused
                if event.key == pygame.K_c:
                    dead_color = random.choice(
                        [(0, 100, 102), (6, 90, 96), (11, 82, 91), (20, 69, 82), (27, 58, 75), (33, 47, 69),
                         (39, 38, 64), (62, 31, 71)]
                    )
                    live_color = random.choice(
                        [(255, 0, 0), (255, 135, 0), (255, 211, 0), (222, 255, 10), (161, 255, 10), (10, 255, 153),
                         (10, 239, 255), (20, 125, 245)]
                    )
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        if not paused:
            for row in board:
                for cell in row:
                    compute_next(board, cell)
            update(Surface, board)
            sleep(0.08)
            pygame.display.flip()
