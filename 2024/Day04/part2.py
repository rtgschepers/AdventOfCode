import time


class Day4:
    grid = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.grid.append(list(line))

    def solve(self):
        xmas_count = 0
        for y in range(1, len(self.grid) - 1):
            for x in range(1, len(self.grid[y]) - 1):
                if self.grid[y][x] == 'A':
                    xmas_count += self.check_neighbours(x, y)
        print('Result: ', xmas_count)

    def check_neighbours(self, x: int, y: int) -> bool:
        diagonals = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
        for offsets in diagonals:
            opposite = None
            for offset_x, offset_y in offsets:
                new_x, new_y = x + offset_x, y + offset_y
                value = self.grid[new_y][new_x]

                if value != 'M' and value != 'S':
                    return False

                if opposite is None:
                    opposite = value
                elif value != ('M' if opposite == 'S' else 'S'):
                    return False
        return True


if __name__ == '__main__':
    start_time = time.time()
    Day4().solve()
    print('Execution time: ' + str(time.time() - start_time))
