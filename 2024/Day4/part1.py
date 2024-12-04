import time


class Day4:
    grid = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.grid.append(list(line))

    def solve(self):
        xmas_count = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 'X':
                    directions = self.check_neighbours(x, y, 'M')
                    for direction in directions:
                        xmas_count += self.check_xmas(x, y, direction)
        print('Result: ', xmas_count)

    def check_neighbours(self, x: int, y: int, char: str) -> list:
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        result_offsets = []

        for offset_x, offset_y in offsets:
            new_x, new_y = x + offset_x, y + offset_y

            value = None
            if 0 <= new_y < len(self.grid) and 0 <= new_x < len(self.grid[0]):
                value = self.grid[new_y][new_x]

            if value == char:
                result_offsets.append((offset_x, offset_y))
        return result_offsets

    def check_xmas(self, x: int, y: int, direction: tuple) -> bool:
        dx, dy = direction
        x, y = x + dx, y + dy

        for c in 'AS':
            x, y = x + dx, y + dy
            if not (0 <= y < len(self.grid)) or not (0 <= x < len(self.grid[0])):
                return False

            if c != self.grid[y][x]:
                return False
        return True


if __name__ == '__main__':
    start_time = time.time()
    Day4().solve()
    print('Execution time: ' + str(time.time() - start_time))
