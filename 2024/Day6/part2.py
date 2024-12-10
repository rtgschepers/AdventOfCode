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
        loops = []
        for path_x, path_y in tqdm(path):
            if (path_x, path_y) in loops:
                continue

            pos = self.start
            cur_path = [pos]

            temp_grid = [x[:] for x in self.grid]
            temp_grid[path_y][path_x] = 'O'

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
                            if (path_x, path_y) not in loops:
                                loops.append((path_x, path_y))
                            break
                    elif next_pos in '#O':
                        i = self.directions.index((dx, dy))
                        if i == len(self.directions) - 1:
                            i = -1
                        pos = (x, y, *self.directions[i + 1])
                except IndexError:
                    break
        print(len(loops))
        '''
        Wrong answers
        2246
        2245
        2247
        489
        488
        490
        2065
        '''

    def get_path(self):
        pos = self.start
        path = [(pos[0], pos[1])]
        while True:
            x, y, dx, dy = pos
            next_x, next_y = x + dx, y + dy
            try:
                next_pos = self.grid[next_y][next_x]
                if next_pos in '.^':
                    pos = (next_x, next_y, dx, dy)
                    if (next_x, next_y) not in path:
                        path.append((next_x, next_y))
                elif next_pos == '#':
                    i = self.directions.index((dx, dy))
                    if i == len(self.directions) - 1:
                        i = -1
                    pos = (x, y, *self.directions[i + 1])
            except IndexError:
                break
        return path[1:]


if __name__ == '__main__':
    time = timeit(lambda: Day6().solve(), number=1)
    print(f'Execution time: {time:.4f}')
