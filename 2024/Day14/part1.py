import re
from timeit import timeit


class Day14:
    width = 101
    height = 103
    seconds = 100
    robots = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.robots.append([int(x) for x in re.findall(r'-*\d+', line)])

    def solve(self):
        cx, cy = self.width // 2, self.height // 2
        q1, q2, q3, q4 = [0 for _ in range(4)]

        for x, y, dx, dy in self.robots:
            x = (dx * self.seconds + x) % self.width
            y = (dy * self.seconds + y) % self.height

            if x < cx and y < cy:
                q1 += 1
            elif x < cx and y > cy:
                q2 += 1
            elif x > cx and y < cy:
                q3 += 1
            elif x > cx and y > cy:
                q4 += 1
        print(q1 * q2 * q3 * q4)


if __name__ == '__main__':
    time = timeit(lambda: Day14().solve(), number=1)
    print(f'Execution time: {time:.4f}')
