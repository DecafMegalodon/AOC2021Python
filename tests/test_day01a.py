import unittest
import day01a

class TestYeah(unittest.TestCase):
    def setUp(self):
        self.input = input = day01a.read_input("./tests/test_inputs/day01input.txt")

    def test_input_read(self):
        self.assertEqual(len(self.input), 10)

    def test_input_format(self):
        self.assertEqual(sum(self.input), 2256)
        
    def test_depth_comparison(self):
        self.assertEqual(day01a.count_deeper(self.input), 7)