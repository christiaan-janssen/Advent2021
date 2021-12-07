#!/usr/bin/env python3

import unittest
from day07 import align_crabs, align_crabs_b, move_to, move_to_2

class TestAlignCrabs(unittest.TestCase):
    def test_align(self):
        test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.assertEqual(align_crabs(test_input), 37)

    def test_move_a_crab(self):
        self.assertEqual(move_to(16, 2), 14)

    def test_move_a_crab_2(self):
        self.assertEqual(move_to_2(16, 5), 66)

    def test_aling_b(self):
        test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.assertEqual(align_crabs_b(test_input), 168)
