import unittest

import kniffel


class TestScores(unittest.TestCase):

    def test_01_numbers(self):

        task = kniffel.Numbers(4)
        self.assertTrue(task._points == 0)
        self.assertTrue(task.do([4, 1, 4, 2, 3]) == 8)
        self.assertTrue(task._points == 8)


if __name__ == '__main__':
    unittest.main()
