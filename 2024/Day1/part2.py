import re
import time


class Day1:
    left = []
    right = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            matches = re.findall(r'\d+', line)
            self.left.append(int(matches[0]))
            self.right.append(int(matches[1]))

    def solve(self):
        ans = 0
        for x in range(len(self.left)):
            ans += self.left[x] * self.right.count(self.left[x])
        print(ans)


if __name__ == '__main__':
    start_time = time.time()
    Day1().solve()
    print('Execution time: ' + str(time.time() - start_time))
