import unittest

from typing import List, Tuple
from move_cars import *

def check_movement_correctness(start: List[int], final: List[int], \
                               moves: List[Tuple[int]]) -> bool:
    """ Method to check correctness of moves
    Args:
        start: list of integers where ith element is the car currently in the
               ith space
        final: list of integers where ith element is the car that should be in
               the ith space
        moves: list of tuples of integers.
               Each move has format (car number, old space, new space)
    Return:
        bool:  is the move correct
    """
    current_pos = start[:]
    for move in moves:
        car, old_space, new_space = move
        if current_pos[new_space] != 0:
            return False
        if current_pos[old_space] != car:
            return False
        current_pos[old_space] = 0
        current_pos[new_space] = car
    return current_pos == final

class TestMoveCars(unittest.TestCase):

    def test_input(self):
        self.assertFalse(check_input([], []))
        self.assertFalse(check_input([1], [1]))
        self.assertFalse(check_input([1], [0]))
        self.assertFalse(check_input([1, 2, 0], [1, 3, 0]))
        self.assertFalse(check_input([0, 1], [0, 1, 1]))
        self.assertFalse(check_input([0, 1, 1], [0, 1]))
        self.assertTrue(check_input([0], [0]))
        self.assertTrue(check_input([3, 2, 1, 0], [1, 0, 3, 2]))

    def test_0_moves(self):
        self.assertEqual(list(generate_moves([0], [0])), [])
        self.assertEqual(list(generate_moves([1, 2, 0], [1, 2, 0])), [])

    def test_1_move(self):
        self.assertEqual(list(generate_moves([1, 0], [0, 1])), \
			[(1, 0, 1)])
        self.assertEqual(list(generate_moves([1, 2, 0], [1, 0, 2])), \
			[(2, 1, 2)])

    def test_correctness(self):
        start, final = [1, 2, 0, 3], [3, 1, 2, 0]
        self.assertTrue(check_movement_correctness(start, final, \
                        list(generate_moves(start, final))))
        self.assertEqual(len(list(generate_moves(start, final))), 3)


if __name__ == '__main__':
    unittest.main()
