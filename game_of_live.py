
import curses
import numpy

from copy import deepcopy

width = 5
height = 5

board = numpy.asarray([[0]*width for i in range(height)])

def print_board(board):
    for row in board:
        print(row)

    print('-'*25)

def neighbours_coordinates(c):
    neighbours = []
    neighbours.append((c[0]-1, c[1]-1))
    neighbours.append((c[0]-1, c[1]))
    neighbours.append((c[0]-1, c[1]+1))
    neighbours.append((c[0], c[1]-1))
    neighbours.append((c[0], c[1]+1))
    neighbours.append((c[0]+1, c[1]-1))
    neighbours.append((c[0]+1, c[1]))
    neighbours.append((c[0]+1, c[1]+1))

    return neighbours

def is_alive(coordinates):
    return int(coordinates)

def valid_coordinates(coordinates):
    if coordinates[0] >= height or coordinates[1] >= width:
        return False

    return True

def live_neighbours(board, coordinates):
    neighbours = 0
    for c in neighbours_coordinates(coordinates):
        if valid_coordinates(c):
            if is_alive(board[c]):
                neighbours += 1

    return neighbours

def alive_cells(board):
    result = []
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if board[i][j] == 1: result.append((i, j))

    return result

def evolve_board(board):
    buffer_board = deepcopy(board)
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            l_n = live_neighbours(board, (i, j))
            if is_alive(board[(i, j)]):
                if l_n > 3 or l_n < 2:
                    buffer_board[(i, j)] = 0
            else:
                if l_n == 3:
                    buffer_board[(i, j)] = 1

    return buffer_board


if __name__ == '__main__':
    board[1][2] = 1
    board[2][2] = 1
    board[3][2] = 1

    print_board(board)
    board = evolve_board(board)
    print_board(board)
    board = evolve_board(board)
    print_board(board)
    board = evolve_board(board)
    print_board(board)
    board = evolve_board(board)
    print_board(board)