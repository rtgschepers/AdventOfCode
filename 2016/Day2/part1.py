class Day2:
    def __init__(self):
        self.instructions = []
        for line in [x.rstrip() for x in open('input.txt')]:
            self.instructions.append(line)
        self.grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.position = [len(self.grid) // 2, len(self.grid) // 2]

    def solve(self):
        code = ''
        for instruction in self.instructions:
            for char in instruction:
                match char:
                    case 'U':
                        self.position[0] = max(0, self.position[0] - 1)
                    case 'D':
                        self.position[0] = min(len(self.grid) - 1, self.position[0] + 1)
                    case 'L':
                        self.position[1] = max(0, self.position[1] - 1)
                    case 'R':
                        self.position[1] = min(len(self.grid[0]) - 1, self.position[1] + 1)
            code += str(self.grid[self.position[0]][self.position[1]])
        print(code)


if __name__ == '__main__':
    Day2().solve()
