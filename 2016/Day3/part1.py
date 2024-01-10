import re


class Day3:
    def __init__(self):
        self.triangles = []
        for line in [x.rstrip() for x in open('input.txt')]:
            self.triangles.append([int(x) for x in re.findall(r'\d+', line)])

    def solve(self):
        possible = 0
        for triangle in self.triangles:
            diag = max(triangle)
            triangle.remove(diag)
            if sum(triangle) > diag:
                possible += 1
        print(possible)


if __name__ == '__main__':
    Day3().solve()
