from collections import Counter

import numpy as np


class Day6:

    def __init__(self):
        with open('input.txt', 'r') as file:
            lines = [list(line.strip()) for line in file]
        self.grid = np.array(lines)

    def solve(self):
        code = ''
        for i in range(len(self.grid[0])):
            col = list(self.grid[:, i])
            most_common, count = Counter(col).most_common()[-1]
            code += most_common
        print(code)


if __name__ == '__main__':
    Day6().solve()
