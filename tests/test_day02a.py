import unittest
import day02a

class TestDay02a(unittest.TestCase):
    def setUp(self):
        self.input = day02a.read_input("./tests/test_inputs/day02input.txt")

    def test_input_read(self):
        self.assertEqual(len(self.input), 6)
        
    def test_submarine_simulator(self):
        self.assertEqual(day02a.simulate_submarine(self.input), 150)
        
    def test_full_solution(self):
        self.assertEqual(day02a.simulate_submarine(day02a.read_input()), 1670340)