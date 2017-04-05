
from copy import deepcopy
from game_of_life import GameOfLife
from nose.tools import assert_equal


class TestGameOfLife(object):

    def setUp(self):
        height, width = 6, 5
        self.g = GameOfLife(height=height, width=width)

    def test_board(self):
        assert_equal(len(self.g.board), self.g.height)
        assert_equal(len(self.g.board[0]), self.g.width)

    def test_set_cell(self):
        temp = deepcopy(self.g)
        temp.board[0][0] = 1
        assert_equal(temp.board[0][0], 1)


