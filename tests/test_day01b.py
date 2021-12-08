import unittest
import day01b

class TestDay01b(unittest.TestCase):
    def setUp(self):
        self.input = day01b.read_input("./tests/test_inputs/day01input.txt")
        self.pooled_input = day01b.calc_sliding_sum(self.input)

    def test_input_read(self):
        self.assertEqual(len(self.input), 10)

    def test_input_format(self):
        self.assertEqual(sum(self.input), 2256)
        
    def test_depth_comparison(self):
        self.assertEqual(day01b.count_deeper(self.pooled_input), 5)
        
    def test_full_solution(self):
        fullinput = day01b.read_input()
        pooled_full = day01b.calc_sliding_sum(fullinput)
        deeper_count = day01b.count_deeper(pooled_full)
        self.assertEqual(deeper_count , 1728)  # Answer confirmed for my input on AoC