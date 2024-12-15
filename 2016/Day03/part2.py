import re


class Day3:
    triangles = []

    def __init__(self):
        temp = []
        for line in [x.rstrip() for x in open('input.txt')]:
            temp.append([int(x) for x in re.findall(r'\d+', line)])

        for x in range(len(temp[0])):
            for y in range(0, len(temp), 3):
                self.triangles.append([temp[y][x], temp[y + 1][x], temp[y + 2][x]])

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
