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
        for number in range(1, 7, 1):
            if np.sum(dice == number) >= self._required:
                return np.sum(dice)
        return 0


class FullHouse(task):

    def __init__(self):
        super.__init__(self, "FullHouse")

    def points(self, dice):
        three = False
        pair = False
        for number in range(1, 7, 1):
            if np.sum(dice == number) == 3:
                three = True
            elif np.sum(dice == number) == 2:
                pair = True
        if three and pair:
            return 25
        else:
            return 0


class SmallStreet(task):

    def __init__(self):
        super.__init(self, "SmallStreet")

    def points(self, dice):
        dices = np.unique(np.sort(dice))
        if np.sum(dices[:-1] + 1 == dices[1:]) >= 3:
            return 30
        return 0


class BigStreet(task):

    def __init__(self):
        super.__init(self, "BigStreet")

    def points(self, dice):
        dices = np.unique(np.sort(dice))
        if np.sum(dices[:-1] + 1 == dices[1:]) >= 4:
            return 40
        return 0


class Kniffel(task):

    def __init__(self):
        super.__init__(self, "Kniffel")

    def points(self, dice):
        if len(np.unique(dice)) == 1:
            return 50
        return 0


class Chance(task):

    def __init__(self):
        super.__init__(self, "Chance")

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
