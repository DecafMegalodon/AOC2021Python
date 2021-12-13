import unittest
import day02a

class TestDay02a(unittest.TestCase):
    def setUp(self):
        self.input = day02a.read_input("./tests/test_inputs/day02input.txt")

    def test_input_read(self):
        self.assertEqual(len(self.input), 6)