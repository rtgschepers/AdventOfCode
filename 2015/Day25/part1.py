import re

import numpy as np


class Day25:
    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.row, self.col = [int(x) for x in re.findall(r'\d+', line)]
            size = (self.row + self.col) + 3
            self.grid = np.zeros([size, size])

    def solve(self):
        self.grid[0][0] = 20151125
        start_row, row, col, max_col = 1, 1, 0, 0

        while not (row == self.row - 1 and col == self.col - 1):
            if row == -1:  # reset
                row = start_row + 1
                start_row = row
                max_col = col - 1
                col = 0

            if col == 0:
                prev_val = self.grid[0][max_col]
            else:
                prev_val = self.grid[row + 1][col - 1]

            next_val = prev_val * 252533 % 33554393
            self.grid[row][col] = next_val

            row -= 1
            col += 1

        print(self.grid[row + 1][col - 1] * 252533 % 33554393)


if __name__ == '__main__':
    Day25().solve()
