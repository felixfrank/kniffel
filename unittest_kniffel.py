import unittest

import game
import kniffel


class TestScores(unittest.TestCase):

    def test_01_numbers(self):

        task = kniffel.Numbers(4)
        self.assertTrue(task._name == "numbers_4")
        self.assertTrue(task._points == 0)
        self.assertTrue(task.do([4, 1, 4, 2, 3]) == 8)
        self.assertTrue(task._points == 8)
        self.assertTrue(task._fulfilled is True)
        self.assertTrue(task.points([2, 1, 4, 4, 4]) == 12)
        self.assertTrue(task._points == 8)

        task = kniffel.Numbers(1)
        self.assertTrue(task._points == 0)
        self.assertTrue(task.do([4, 1, 4, 2, 3]) == 1)
        self.assertTrue(task._points == 1)
        self.assertTrue(task._fulfilled is True)
        self.assertTrue(task.points([1, 1, 1, 1, 1]) == 5)
        self.assertTrue(task._points == 1)

    def test_02_street(self):

        task = kniffel.SmallStreet()
        self.assertTrue(task.points([4, 2, 1, 6, 6]) == 0)
        self.assertTrue(task._fulfilled is False)
        self.assertTrue(task.do([4, 2, 1, 6, 3]) == 30)
        self.assertTrue(task._fulfilled is True)

        task = kniffel.BigStreet()
        self.assertTrue(task.points([6, 2, 5, 4, 3]) == 40)
        self.assertTrue(task.points([6, 2, 5, 4, 4]) == 0)
        self.assertTrue(task.points([1, 2, 3, 4, 6]) == 0)
        self.assertTrue(task.points([1, 2, 3, 4, 4]) == 0)

    def test_03_kniffel(self):

        task = kniffel.Kniffel()
        self.assertTrue(task.points([1, 1, 1, 1, 1]) == 50)
        self.assertTrue(task.points([2, 2, 2, 2, 2]) == 50)
        self.assertTrue(task.points([3, 3, 3, 3, 3]) == 50)
        self.assertTrue(task.points([4, 4, 4, 4, 4]) == 50)
        self.assertTrue(task.points([5, 5, 5, 5, 5]) == 50)
        self.assertTrue(task.points([6, 6, 6, 6, 6]) == 50)
        self.assertTrue(task.points([4, 2, 1, 6, 6]) == 0)
        self.assertTrue(task.points([1, 2, 1, 1, 1]) == 0)
        for i in range(100):
            dice = game.roll_dices(5)
            if (dice == dice[0]).all():
                continue
            self.assertTrue(task.points(dice) == 0)

    def test_04_XOfAKind(self):

        task = kniffel.XOfAKind(3)
        self.assertTrue(task.points([1, 2, 3, 4, 5]) == 0)
        self.assertTrue(task.points([1, 1, 3, 4, 5]) == 0)
        self.assertTrue(task.points([1, 1, 1, 4, 5]) == 12)
        self.assertTrue(task.points([6, 1, 6, 4, 6]) == 23)
        self.assertTrue(task.points([6, 6, 6, 4, 6]) == 28)
        self.assertTrue(task.points([6, 3, 6, 4, 1]) == 0)


if __name__ == '__main__':
    unittest.main()
