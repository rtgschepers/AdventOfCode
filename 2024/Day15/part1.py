from timeit import timeit


class Day15:
    grid = []
    moves = ''
    pos = (int, int)

    def __init__(self):
        grid = True
        for line in [x.rstrip() for x in open('input.txt')]:
            if line == '':
                grid = False
            elif grid:
                self.grid.append(list(line))
                if (i := line.find('@')) > -1:
                    self.pos = (i, len(self.grid) - 1)
                pass
            else:
                self.moves += line

    def solve(self):
        for move in self.moves:
            x, y, dx, dy = *self.pos, *self.get_direction(move)
            updates = []
            while True:
                new_x, new_y = x + dx, y + dy
                if self.grid[new_y][new_x] == '.':
                    updates.append((x, y, new_x, new_y))
                    break
                elif self.grid[new_y][new_x] == 'O':
                    updates.append((x, y, new_x, new_y))
                    x, y = new_x, new_y
                elif self.grid[new_y][new_x] == '#':
                    updates = []
                    break
            for ox, oy, nx, ny in reversed(updates):
                symbol = self.grid[oy][ox]
                self.grid[ny][nx] = symbol
                self.grid[oy][ox] = '.'
                if symbol == '@':
                    self.pos = (nx, ny)
        total = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == 'O':
                    total += 100 * y + x
        print(total)

    def get_direction(self, move: str) -> (int, int):
        match move:
            case '^':
                return 0, -1
            case '>':
                return 1, 0
            case 'v':
                return 0, 1
            case '<':
                return -1, 0


if __name__ == '__main__':
    time = timeit(lambda: Day15().solve(), number=1)
    print(f'Execution time: {time:.4f}')
