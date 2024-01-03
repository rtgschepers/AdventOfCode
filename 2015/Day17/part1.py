class Day17:
    containers = []
    limit = 150
    combinations = 0

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.containers.append(int(line))

    def solve(self):
        self.find_combinations(self.limit, 0)
        print(self.combinations)

    def find_combinations(self, total, index):
        for i in range(index, len(self.containers)):
            new_total = total - self.containers[i]
            if new_total > 0:
                self.find_combinations(new_total, i + 1)
            if new_total == 0:
                self.combinations += 1


if __name__ == '__main__':
    Day17().solve()
