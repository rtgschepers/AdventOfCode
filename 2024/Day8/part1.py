import re
from timeit import timeit


class Day8:
    grid = []
    layout = {}

    def __init__(self):
        for y, line in enumerate([x.rstrip() for x in open('test.txt')]):
            for match in re.finditer(r'((?!\.).)', line):
                symbol = match.group()
                if symbol not in self.layout:
                    self.layout[symbol] = []
                self.layout[symbol].append((match.start(), y))
            self.grid.append(line)

    def solve(self):
        pass


if __name__ == '__main__':
    time = timeit(lambda: Day8().solve(), number=1)
    print(f'Execution time: {time:.4f}')
