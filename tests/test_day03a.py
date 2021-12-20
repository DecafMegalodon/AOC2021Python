import unittest
import day03a

class TestDay03a(unittest.TestCase):
    
    def setUp(self):
        self.input = day03a.read_input("./tests/test_inputs/day03input.txt")

    def test_input(self):
        self.assertEqual(len(self.input), 12)  # There should be 12 lines of test input