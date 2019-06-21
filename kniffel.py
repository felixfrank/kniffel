import numpy as np


nturns = 13
p = np.ones(6) / 6


TASKS = []


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
        super.__init__(self, "numbers_%i" % n)
        self.n = n

    def points(self, dice):
        return self.n * np.sum(dice == self.n)



class XOfAKind(task):

    def __init__(self, n):
        self._required = n
        if n == 3:
            super.__init__(self, "ThreeOfAKind")
        elif n == 4:
            super.__init__(self, "FourOfAKind")
        else:
            raise ValueError("Only three or four of a kind exist.")


    def points(self, dice):
        for number in range(1, 7, 1):
            if np.sum(dice == number) >= self._required:
                return np.sum(dice)
            else:
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
        dices = np.sort(dices)
        if np.sum(dices[:-1] + 1 == dices[1:]) >= 3:
            return 30
        return 0


class BigStreet(task):

    def __init__(self):
        super.__init(self, "BigStreet")

    def points(self, dice):
        dices = np.sort(dices)
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


def roll_dices(n):
    return np.random.choice(6, size=n, p=p)


class Chance(task):

    def __init__(self):
        super.__init__(self, "Chance")

    def points(self, dice):
        return np.sum(dice)


for i in range(nturns):
