import re
from timeit import timeit


class Day2:
    data = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            for x in line.split(','):
                self.data.append([int(y) for y in x.split('-')])

    def solve(self):
        invalids = []
        for a, b in self.data:
            for x in range(a, b + 1):
                x = str(x)
                for y in range(len(x)//2, 0, -1):
                    if len(x) % y != 0:
                        continue

                    m = re.findall(rf'([\d+]{{{y}}})', x)
                    if len(set(m)) == 1 < len(m):
                        invalids.append(x)
        print(sum(int(x) for x in set(invalids)))


if __name__ == '__main__':
    time = timeit(lambda: Day2().solve(), number=1)
    print(f'Execution time: {time:.4f}')
