from collections import deque
from timeit import timeit
from typing import Deque


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
                line = ''.join([x for x in line for _ in (0, 1)])
                line = line.replace('OO', '[]')
                line = line.replace('@@', '@.')

                self.grid.append(list(line))
                if (i := line.find('@')) > -1:
                    self.pos = (i, len(self.grid) - 1)
                pass
            else:
                self.moves += line

    def solve(self):
        for i, move in enumerate(self.moves):
            if self.pos == (3, 7) and move == '^':
                pass
            changes: Deque[(int, int, int, int)] = deque([(*self.pos, *self.get_direction(move))])
            update_queue = []

            while len(changes):
                x, y, dx, dy = changes.popleft()
                new_x, new_y = x + dx, y + dy

                if self.grid[new_y][new_x] == '.':
                    update_queue.append((x, y, new_x, new_y))
                elif self.grid[new_y][new_x] in '[]':
                    update_queue.append((x, y, new_x, new_y))
                    if (new_x, new_y, dx, dy) not in changes:
                        changes.append((new_x, new_y, dx, dy))

                    if dy != 0:
                        other = 1 if self.grid[new_y][new_x] == '[' else -1
                        if (new_x + other, new_y, dx, dy) not in changes:
                            changes.append((new_x + other, new_y, dx, dy))
                elif self.grid[new_y][new_x] == '#':
                    update_queue = []
                    break

            for ox, oy, nx, ny in reversed(update_queue):
                symbol = self.grid[oy][ox]
                self.grid[ny][nx] = symbol
                self.grid[oy][ox] = '.'
                if symbol == '@':
                    self.pos = (nx, ny)

        total = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == '[':
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
