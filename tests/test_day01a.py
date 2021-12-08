import unittest
import day01a

class TestDay01a(unittest.TestCase):
    def setUp(self):
        self.input = day01a.read_input("./tests/test_inputs/day01input.txt")

    def test_input_read(self):
        self.assertEqual(len(self.input), 10)

    def test_input_format(self):
        self.assertEqual(sum(self.input), 2256)
        
    def test_depth_comparison(self):
        self.assertEqual(day01a.count_deeper(self.input), 7)
        
    def test_full_solution(self):
        fullinput = day01a.read_input()
        deeper_count = day01a.count_deeper(fullinput)
        self.assertEqual(deeper_count , 1688)  # Answer confirmed for my input on AoC