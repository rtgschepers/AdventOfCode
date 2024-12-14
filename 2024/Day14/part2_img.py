import re
from timeit import timeit

import numpy as np
from PIL import Image


class Day14:
    width = 101
    height = 103
    robots = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.robots.append([int(x) for x in re.findall(r'-*\d+', line)])

    def solve(self):
        for i in range(1, self.width * self.height):
            for r in range(len(self.robots)):
                x, y, dx, dy = self.robots[r]
                x, y = (dx + x) % self.width, (dy + y) % self.height
                self.robots[r] = (x, y, dx, dy)
            self.save_img(i)

    def save_img(self, iteration):
        grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for x, y, _, _ in self.robots:
            grid[y][x] = 1
        image = Image.fromarray(np.array(grid, dtype=np.uint8) * 255)
        image.save(f'output/{iteration}.png')


if __name__ == '__main__':
    time = timeit(lambda: Day14().solve(), number=1)
    print(f'Execution time: {time:.4f}')
