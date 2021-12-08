import unittest
import day01a

class TestYeah(unittest.TestCase):
    def test_input_read(self):
        input = day01a.read_input("./tests/test_inputs/day01input.txt")
        self.assertEqual(len(input), 10)