
import numpy
import curses
import drawille

from random import randrange
from copy import deepcopy

class GameOfLife(object):

    def __init__(self, **kwargs):
        self.height = kwargs['height']
        self.width = kwargs['width']
        self.board = numpy.asarray([[0]*self.width for i in range(self.height)])

    def neighbours_coordinates(self, coordinates):
        neighbours = []
        neighbours.append((coordinates[0]-1, coordinates[1]-1))
        neighbours.append((coordinates[0]-1, coordinates[1]))
        neighbours.append((coordinates[0]-1, coordinates[1]+1))
        neighbours.append((coordinates[0], coordinates[1]-1))
        neighbours.append((coordinates[0], coordinates[1]+1))
        neighbours.append((coordinates[0]+1, coordinates[1]-1))
        neighbours.append((coordinates[0]+1, coordinates[1]))
        neighbours.append((coordinates[0]+1, coordinates[1]+1))

        return neighbours

    def is_alive(self, coordinates):
        return int(coordinates)

    def valid_coordinates(self, coordinates):
        if coordinates[0] >= self.height or coordinates[1] >= self.width:
            return False

        return True

    def live_neighbours(self, coordinates):
        neighbours = 0
        for c in self.neighbours_coordinates(coordinates):
            if self.valid_coordinates(c):
                if self.is_alive(self.board[c]):
                    neighbours += 1

        return neighbours

    def alive_cells(self):
        result = []
        for i, row in enumerate(self.board):
            for j, column in enumerate(row):
                if self.board[i][j] == 1: result.append((i, j))

        return result

    def evolve_board(self):
        buffer_board = deepcopy(self.board)
        for i, row in enumerate(self.board):
            for j, column in enumerate(row):
                l_n = self.live_neighbours((i, j))
                if self.is_alive(self.board[(i, j)]):
                    if l_n > 3 or l_n < 2:
                        buffer_board[(i, j)] = 0
                else:
                    if l_n == 3:
                        buffer_board[(i, j)] = 1

        self.board = buffer_board

def main():
    width, height = drawille.getTerminalSize()
    game = GameOfLife(width=(int(width*2.0)-2), height=(int(height*4.0))-4)
    
    def fill_board_randomly(game):
        for y in range(game.height):
            for x in range(game.width):
                game.board[y][x] = randrange(2)
        
    fill_board_randomly(game)             
    
    def frame_coordinates(game):
        while True:
            game.evolve_board()
            s = []
            for y in range(game.height):
                for x in range(game.width):
                    if game.board[y][x] == 1: s.append((x, y))

            yield s
     
    s = drawille.Canvas()
    drawille.animate(s, frame_coordinates, 1./5, game)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

