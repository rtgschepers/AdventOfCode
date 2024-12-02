import re


class Day1:
    left = []
    right = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            matches = re.findall(r'\d+', line)
            self.left.append(int(matches[0]))
            self.right.append(int(matches[1]))

            self.left.sort()
            self.right.sort()

    def solve(self):
        ans = 0
        for x in range(len(self.left)):
            ans += abs(self.left[x] - self.right[x])
        print(ans)


if __name__ == '__main__':
    Day1().solve()
