import re
from timeit import timeit


class Day1:
    nums = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            num = int(re.findall(r'\d+', line)[0])
            self.nums.append(num * (1 if line[0] == 'L' else -1))

    def solve(self):
        pos = 50
        ans = 0
        for num in self.nums:
            pos += num
            pos %= 100
            ans += 1 if pos == 0 else 0
        print(ans)


if __name__ == '__main__':
    time = timeit(lambda: Day1().solve(), number=1)
    print(f'Execution time: {time:.4f}')
