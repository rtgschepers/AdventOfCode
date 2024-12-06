from timeit import timeit


class Day6:
    grid = []
    start = (int, int)
    repeat_count = 10
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self):
        for line in [x.rstrip() for x in open('test.txt')]:
            if '^' in line:
                self.start = (line.index('^'), len(self.grid))
            self.grid.append(list(line))

    def solve(self):
        loop_count = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                pos = self.start
                direction = self.directions[0]
                temp_grid = [x[:] for x in self.grid]
                temp_grid[y][x] = '#'
                path = [pos]
                repeat = []

                while True:
                    next_x, next_y = tuple(a + b for a, b in zip(pos, direction))
                    try:
                        next_pos = temp_grid[next_y][next_x]
                        if next_pos in '.^':
                            pos = (next_x, next_y)
                            if pos not in path:
                                repeat = []
                                path.append(pos)
                            elif pos in path and len(repeat) < self.repeat_count:
                                repeat.append(pos)
                            elif pos in path and len(repeat) >= self.repeat_count:
                                loop_count += 1
                                break
                        elif next_pos == '#':
                            i = self.directions.index(direction)
                            if i == len(self.directions) - 1:
                                i = -1
                            direction = self.directions[i + 1]
                    except IndexError:
                        break
        print(loop_count)


if __name__ == '__main__':
    time = timeit(lambda: Day6().solve(), number=1)
    print(f'Execution time: {time:.4f}')
