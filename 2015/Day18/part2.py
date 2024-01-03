import copy


class Day18:
    grid = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.grid.append(list(line))

    def solve(self):
        for i in range(100):
            self.grid = self.update_grid()
        print(sum([x.count('#') for x in self.grid]))

    def update_grid(self):
        temp = copy.deepcopy(self.grid)
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if not self.is_corner(x, y):
                    temp[y][x] = self.update_cell(x, y, self.count_on_neighbours(x, y))
        return temp

    def is_corner(self, x, y):
        return ((x == 0 and y == 0) or
                (x == 0 and y == len(self.grid) - 1) or
                (x == len(self.grid[0]) - 1 and y == 0) or
                (x == len(self.grid[0]) - 1 and y == len(self.grid) - 1))

    def update_cell(self, x, y, on_neighbours):
        if ((self.grid[y][x] == '.' and on_neighbours == 3) or
                (self.grid[y][x] == '#' and on_neighbours in [2, 3])):
            return '#'
        else:
            return '.'

    def count_on_neighbours(self, x, y):
        count_on = 0
        indices = [
            (y - 1, x - 1),
            (y - 1, x),
            (y - 1, x + 1),
            (y, x - 1),
            (y, x + 1),
            (y + 1, x - 1),
            (y + 1, x),
            (y + 1, x + 1),
        ]

        for nb_y, nb_x in indices:
            if -1 < nb_y < len(self.grid) and -1 < nb_x < len(self.grid[0]) and self.grid[nb_y][nb_x] == '#':
                count_on += 1
        return count_on


if __name__ == '__main__':
    Day18().solve()
