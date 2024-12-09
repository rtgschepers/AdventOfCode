from timeit import timeit

from tqdm import tqdm


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
        path = self.get_path()
        loop_count = 0
        for path_x, path_y, path_dx, path_dy in tqdm(path):
            if self.grid[path_y][path_x] != '.':
                continue

            pos = self.start
            cur_path = [pos]

            temp_grid = [x[:] for x in self.grid]
            temp_grid[path_y][path_x] = '#'

            while True:
                x, y, dx, dy = pos
                next_x, next_y = x + dx, y + dy
                try:
                    next_pos = temp_grid[next_y][next_x]
                    if next_pos in '.^':
                        pos = (next_x, next_y, dx, dy)
                        if pos not in cur_path:
                            cur_path.append(pos)
                        else:
                            loop_count += 1
                            break
                    elif next_pos == '#':
                        i = self.directions.index((dx, dy))
                        if i == len(self.directions) - 1:
                            i = -1
                        pos = (x, y, *self.directions[i + 1])
                except IndexError:
                    break
        print(loop_count)
        '''
        Wrong answers
        2246
        2245
        2247
        '''

    def get_path(self):
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
        return path


if __name__ == '__main__':
    time = timeit(lambda: Day6().solve(), number=1)
    print(f'Execution time: {time:.4f}')
