"""
@author Shay Peleg
Conways - THE GAME OF LIFE

Controls:
p = Pause Game
u = unPause Game
q = Quit Game
"""

import random
import sys
from time import sleep

import pygame

BoardX = 30
BoardY = 20
dead_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
live_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class Cell:
    """
    class that defines a cell in the game
    @:param state- the current state of the cell- live/dead
    """

    def __init__(self, location):
        """
        initiate a cell- default state=live,
        set neighbor locations according to the cell location
        """
        self.state = random.choice(['live', 'dead'])
        self.location = location  # tuple of location in board matrix (x,y)
        self.neighborLocs = [(x, y) for x in range(self.location[0] - 1, self.location[0] + 2) for y in
                             range(self.location[1] - 1, self.location[1] + 2) if
                             (x, y) != self.location and 0 <= x < BoardX and 0 <= y < BoardY]
        self.nextState = None

    def __str__(self):
        if self.state == 'live':
            return 'O'
        return 'X'

    def get_state(self):
        return self.state


class GameBoard:
    """
    initiate the game board and cells
    """

    def __init__(self, surface):
        self.board = {(x, y): Cell((x, y)) for x in range(BoardX) for y in range(BoardY)}
        for cell in self.board.values():
            pygame.draw.rect(surface, live_color,
                             (cell.location[0] * 8, cell.location[1] * 8, 8 - 1, 8 - 1))

    def computeNextState(self, cell):
        """

        :param cell:a cell on the board
        :return:None
        """
        neighbor_stats = []
        for neighbor in cell.neighborLocs:
            neighbor_stats.append(self.board[neighbor].state)
        count = neighbor_stats.count('live')
        # game logic:
        if cell.state == 'live':
            if count <= 1 or count > 3:
                cell.nextState = 'dead'
            neighbor_stats = []
        else:
            if count == 3:
                cell.nextState = 'live'
            neighbor_stats = []

    def UpdateBoard(self, surface):
        """

        :param surface: a surface pygame object (UI representation of the game board)
        :return: None
        """
        for cell in self.board.values():
            if cell.nextState == 'live':
                col = live_color
                pygame.draw.rect(surface, col, (cell.location[0] * 8, cell.location[1] * 8, 8 - 1, 8 - 1))
                cell.state = cell.nextState
            else:
                col = dead_color
                pygame.draw.rect(surface, col, (cell.location[0] * 8, cell.location[1] * 8, 8 - 1, 8 - 1))
                cell.state = cell.nextState


paused = False
if __name__ == '__main__':
    pygame.init()
    Surface = pygame.display.set_mode((BoardX * 8, BoardY * 8))
    pygame.display.set_caption('THE GAME OF LIFE')
    game = GameBoard(Surface)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True
                if event.key == pygame.K_u:
                    paused = False
                if event.key == pygame.K_c:
                    live_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    dead_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        if not paused:
            for cell in game.board.values():
                game.computeNextState(cell)
            game.UpdateBoard(Surface)
            sleep(0.08)
            pygame.display.flip()
