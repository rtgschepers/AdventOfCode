class Day2:
    def __init__(self):
        self.instructions = []
        for line in [x.rstrip() for x in open('input.txt')]:
            self.instructions.append(line)
        self.grid = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]
        self.position = [2, 0]

    def solve(self):
        code = ''
        for instruction in self.instructions:
            for char in instruction:
                match char:
                    case 'U':
                        new_y = max(0, self.position[0] - 1)
                        if self.grid[new_y][self.position[1]] != 0:
                            self.position[0] = new_y
                    case 'D':
                        new_y = min(len(self.grid) - 1, self.position[0] + 1)
                        if self.grid[new_y][self.position[1]] != 0:
                            self.position[0] = new_y
                    case 'L':
                        new_x = max(0, self.position[1] - 1)
                        if self.grid[self.position[0]][new_x] != 0:
                            self.position[1] = new_x
                    case 'R':
                        new_x = min(len(self.grid[0]) - 1, self.position[1] + 1)
                        if self.grid[self.position[0]][new_x] != 0:
                            self.position[1] = new_x
            code += str(self.grid[self.position[0]][self.position[1]])
        print(code)


if __name__ == '__main__':
    Day2().solve()
