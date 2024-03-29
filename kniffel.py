import numpy as np


class task(object):
    """Baseclass for individual tasks."""

    def __init__(self, name):
        self._fulfilled = False
        self._name = name
        self._points = 0

    def name(self):
        return self._name

    def points(self, dice):
        pass

    def do(self, dice):
        if self._fulfilled:
            return -1
        else:
            self._fulfilled = True
            self._points = self.points(dice)
            return self._points


class Numbers(task):

    def __init__(self, n):
        super(Numbers, self).__init__("numbers_%i" % n)
        self.n = n

    def points(self, dice):
        return self.n * np.sum(np.array(dice) == self.n)


class XOfAKind(task):

    def __init__(self, n):
        self._required = n
        if n == 3:
            super(XOfAKind, self).__init__("ThreeOfAKind")
        elif n == 4:
            super(XOfAKind, self).__init__("FourOfAKind")
        else:
            raise ValueError("Only three or four of a kind exist.")

    def points(self, dice):
        dice = np.array(dice)
        for number in range(1, 7, 1):
            if np.sum(dice == number) >= self._required:
                return np.sum(dice)
        return 0


class FullHouse(task):

    def __init__(self):
        super(FullHouse, self).__init__("FullHouse")

    def points(self, dice):
        if len(np.unique(dice)) == 2:
            c = np.sum(np.array(dice) == dice[0])
            if (c >= 2) and (c <= 3):
                return 25
        return 0


class SmallStreet(task):

    def __init__(self):
        super(SmallStreet, self).__init__("SmallStreet")

    def points(self, dice):
        dices = np.unique(np.sort(dice))
        if np.sum(dices[:-1] + 1 == dices[1:]) >= 3:
            return 30
        return 0


class BigStreet(task):

    def __init__(self):
        super(BigStreet, self).__init__("BigStreet")

    def points(self, dice):
        dices = np.unique(np.sort(dice))
        if np.sum(dices[:-1] + 1 == dices[1:]) >= 4:
            return 40
        return 0


class Kniffel(task):

    def __init__(self):
        super(Kniffel, self).__init__("Kniffel")

    def points(self, dice):
        if len(np.unique(dice)) == 1:
            return 50
        return 0


class Chance(task):

    def __init__(self):
        super(Chance, self).__init__("Chance")

    def points(self, dice):
        return np.sum(dice)


class Tasks:

    def __init__(self):
        self.score = 0
        self.tasks = [Numbers(i) for i in np.arange(1, 7, 1)]
        self.tasks += SmallStreet()
        self.tasks += BigStreet()
        self.tasks += FullHouse()
        self.tasks += XOfAKind(3)
        self.tasks += XOfAKind(4)
        self.tasks += Kniffel()
        self.tasks += Chance()

    def get_score(self):
        return np.sum([_task._points for _task in self.tasks])

    def get_fulfilled(self):
        return np.array([_task._fulfilled for _task in self.tasks])

    def get_numbers_score(self):
        return np.sum([_task._points for _task in self.tasks[:6]])
