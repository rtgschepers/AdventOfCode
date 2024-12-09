from timeit import timeit


class Day6:
    grid = []
    start = (int, int, int, int)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            if '^' in line:
                self.start = (line.index('^'), len(self.grid), *self.directions[0])
            self.grid.append(list(line))

    def solve(self):
        pos = self.start
        path = [pos]
        while True:
            x, y, dx, dy = pos
            next_x, next_y = x + dx, y + dy
            try:
                next_pos = self.grid[next_y][next_x]
                if next_pos in '.^':
                    pos = (next_x, next_y, dx, dy)
                    if pos not in path:
                        path.append(pos)
                elif next_pos == '#':
                    i = self.directions.index((dx, dy))
                    if i == len(self.directions) - 1:
                        i = -1
                    pos = (x, y, *self.directions[i + 1])
            except IndexError:
                break

        unique_path = []
        for x, y, dx, dy in path:
            if (x, y) not in unique_path:
                unique_path.append((x, y))
        print(len(path))
        print(len(unique_path))


if __name__ == '__main__':
    time = timeit(lambda: Day6().solve(), number=1)
    print(f'Execution time: {time:.4f}')
