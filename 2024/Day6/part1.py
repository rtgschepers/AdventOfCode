from timeit import timeit


class Day6:
    grid = []
    path = []
    pos = (int, int)
    direction = (0, -1)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            if '^' in line:
                self.pos = (line.index('^'), len(self.grid))
            self.grid.append(list(line))

    def solve(self):
        self.path.append(self.pos)
        while True:
            next_x, next_y = tuple(a + b for a, b in zip(self.pos, self.direction))
            try:
                next_pos = self.grid[next_y][next_x]
                if next_pos in '.^':
                    self.pos = (next_x, next_y)
                    if self.pos not in self.path:
                        self.path.append(self.pos)
                elif next_pos == '#':
                    i = self.directions.index(self.direction)
                    if i == len(self.directions) - 1:
                        i = -1
                    self.direction = self.directions[i + 1]
            except IndexError:
                break
        print(len(self.path))


if __name__ == '__main__':
    time = timeit(lambda: Day6().solve(), number=1)
    print(f'Execution time: {time:.4f}')
