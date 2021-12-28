import unittest
import pytest
from ..knight_move import knight_move
from ..knights_collision import knights_collision


def test_knight_move():
    assert knight_move((1, 1), (1, 1)) == 0
    assert knight_move((1, 2), (6, 4)) == 3
    assert knight_move((8, 1), (7, 4)) == 2
    assert knight_move((1, 7), (3, 5)) == 4
    assert knight_move((2, 2), (8, 8)) == 4


def test_knights_collision():
    assert knights_collision((1, 2), (3, 4)) == 2
    assert knights_collision((2, 2), (8, 7)) == 0
    assert knights_collision((1, 1), (5, 4)) == 0
    assert knights_collision((5, 1), (7, 5)) == 1
    assert knights_collision((2, 2), (2, 2)) == 0
    assert knights_collision((1, 1), (7, 7)) == 2




@pytest.mark.parametrize("a", [((1, 1), (8, 8)), ((1, 1), (6, 1))])
def test_example(a):
    k1, k2 = a
    assert knight_move(k1, k2)


@pytest.fixture()
def param():
    return (1, 7), (3, 3)


def test_for_fixture(param):
    k1, k2 = param
    assert knight_move(k1, k2) == 2
    assert knights_collision(k1, k2) == 1


class KnightMoveTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(knight_move((1, 2), (6, 4)), 3)

