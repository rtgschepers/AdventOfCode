import re
import time


class Day2:
    lines = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.lines.append([int(x) for x in re.findall(r'\d+', line)])

    def solve(self):
        safe_lines = 0
        for line in self.lines:
            if self.is_safe(line):
                safe_lines += 1
        print(safe_lines)

    def is_safe(self, line):
        increasing = None

        for x in range(len(line) - 1):
            diff = line[x + 1] - line[x]
            if abs(diff) < 1 or abs(diff) > 3:
                return False

            if increasing is None:
                increasing = True if diff > 0 else False

            if increasing and diff < 0:
                return False
            elif not increasing and diff > 0:
                return False

        return True


if __name__ == '__main__':
    start_time = time.time()
    Day2().solve()
    print(time.time() - start_time)
