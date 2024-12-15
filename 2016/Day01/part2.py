class Day1:

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.instructions = [[x[0], int(x[1:])] for x in line.split(', ')]
            self.direction = 'N'
            self.position = [0, 0]
            self.visited = [self.position.copy()]
            pass

    def solve(self):
        for turn, distance in self.instructions:
            self.rotate(turn)
            self.move(distance)
            self.add_to_path()
        print(abs(self.position[0]) + abs(self.position[1]))

    def rotate(self, turn):
        if turn == 'R':
            match self.direction:
                case 'N':
                    self.direction = 'E'
                case 'E':
                    self.direction = 'S'
                case 'S':
                    self.direction = 'W'
                case 'W':
                    self.direction = 'N'
        else:
            match self.direction:
                case 'N':
                    self.direction = 'W'
                case 'E':
                    self.direction = 'N'
                case 'S':
                    self.direction = 'E'
                case 'W':
                    self.direction = 'S'

    def move(self, distance):
        match self.direction:
            case 'N':
                self.position[0] += distance
            case 'E':
                self.position[1] += distance
            case 'S':
                self.position[0] -= distance
            case 'W':
                self.position[1] -= distance

    def add_to_path(self):
        last_pos = self.visited[-1]
        y_step = -1 if last_pos[0] > self.position[0] else 1
        x_step = -1 if last_pos[1] > self.position[1] else 1

        for y in range(last_pos[0], self.position[0] + y_step, y_step):
            for x in range(last_pos[1], self.position[1] + x_step, x_step):
                if [y, x] == last_pos:
                    continue

                if [y, x] in self.visited:
                    print(abs(y) + abs(x))
                    exit()
                self.visited.append([y, x])


if __name__ == '__main__':
    Day1().solve()
