#!/usr/bin/env python3

import unittest
from find_alphabet import is_correct, find_one_alphabet, find_incorrect, fix_incorrect


class TestDictionary(unittest.TestCase):
    def test_is_correct(self):
        self.assertEqual(is_correct(['ART', 'RAT', 'CAT']), True)
        self.assertEqual(is_correct(['ART', 'RAT', 'CAT', 'CAR']), True)
        self.assertEqual(is_correct(['ART', 'RAT', 'CAT', 'CAR', 'CAT']), False)

    def test_find_one_alphabet(self):
        self.assertIn(find_one_alphabet(['ART', 'RAT', 'CAT']), [['T', 'A', 'R', 'C'], ['A', 'T', 'R', 'C'], ['A', 'R', 'T', 'C'], ['A', 'R', 'C', 'T']])
        self.assertIn(find_one_alphabet(['ART', 'RAT', 'CAT', 'CAR']), [['T', 'A', 'R', 'C'], ['A', 'T', 'R', 'C']])

    def test_find_incorrect(self):
        self.assertEqual(sorted(find_incorrect(['ART', 'RAT', 'CAT', 'CAR', 'ACT'])), ['A', 'C', 'R'])

    def test_fix_incorrect(self):
        self.assertEqual(fix_incorrect(['ART', 'RAT', 'CAT', 'CAR', 'ACT']), ['ART', 'RAT', 'CAT', 'CAR'])


if __name__ == "__main__":
    unittest.main()
