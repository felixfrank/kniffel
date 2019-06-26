import numpy as np

nturns = 13
p = np.ones(6) / 6


def roll_dices(n):
    return np.random.choice(6, size=n, p=p)


if __name__ == '__main__':
    for i in range(nturns):
        _dices = roll_dices(6)
