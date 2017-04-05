# -*- coding: utf-8 -*-

import sys
import drawille
from game_of_life import GameOfLife

from random import randrange

def main():
    width, height = drawille.getTerminalSize()
    game = GameOfLife(width=(int(width*2.0)-2), height=(int(height*4.0))-4)
    
    def fill_board_randomly(game):
        def set_cell_randomly():
            if randrange(10) > randrange(6, 10): return 1
            return 0

        for y in range(game.height):
            for x in range(game.width):
                game.board[y][x] = set_cell_randomly()
        
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

