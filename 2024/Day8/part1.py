import re
from timeit import timeit


class Day8:
    grid = []
    layout = {}

    def __init__(self):
        for y, line in enumerate([x.rstrip() for x in open('input.txt')]):
            for match in re.finditer(r'((?!\.).)', line):
                symbol = match.group()
                if symbol not in self.layout:
                    self.layout[symbol] = []
                self.layout[symbol].append((match.start(), y))
            self.grid.append(line)

    def solve(self):
        antinodes = []
        for x in self.layout.values():
            for a in range(len(x) - 1):
                for b in range(a + 1, len(x)):
                    p1_x, p1_y, p2_x, p2_y = *x[a], *x[b]
                    dx, dy = p1_x - p2_x, p1_y - p2_y

                    new_pos = self.is_in_bounds(p1_x + dx, p1_y + dy)
                    if new_pos is not None and new_pos not in antinodes:
                        antinodes.append(new_pos)
                    new_pos = self.is_in_bounds(p2_x + dx * -1, p2_y + dy * -1)
                    if new_pos is not None and new_pos not in antinodes:
                        antinodes.append(new_pos)
        print(len(antinodes))

    def is_in_bounds(self, x: int, y: int) -> tuple | None:
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            return x, y
        return None


if __name__ == '__main__':
    time = timeit(lambda: Day8().solve(), number=1)
    print(f'Execution time: {time:.4f}')
