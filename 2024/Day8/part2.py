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

                    new_nodes = self.get_antinodes(p1_x, p1_y, dx, dy)
                    for node in new_nodes:
                        if node not in antinodes:
                            antinodes.append(node)

                    new_nodes = self.get_antinodes(p2_x, p2_y, dx * -1, dy * -1)
                    for node in new_nodes:
                        if node not in antinodes:
                            antinodes.append(node)
        print(len(antinodes))

    def get_antinodes(self, x: int, y: int, dx: int, dy: int):
        antinodes = []
        while self.is_in_bounds(x, y):
            antinodes.append((x, y))
            x, y = x + dx, y + dy
        return antinodes

    def is_in_bounds(self, x: int, y: int) -> tuple | None:
        if 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]):
            return x, y
        return None


if __name__ == '__main__':
    time = timeit(lambda: Day8().solve(), number=1)
    print(f'Execution time: {time:.4f}')
