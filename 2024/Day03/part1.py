import re
import time


class Day3:
    instructions = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.instructions += re.findall(r'mul\((\d+),(\d+)\)', line)

    def solve(self):
        ans = 0
        for x in self.instructions:
            ans += int(x[0]) * int(x[1])
        print(ans)


if __name__ == '__main__':
    start_time = time.time()
    Day3().solve()
    print('Execution time: ' + str(time.time() - start_time))
