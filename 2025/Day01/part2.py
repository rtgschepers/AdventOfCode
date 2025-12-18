import re
from timeit import timeit

class Day1:

    def __init__(self, *args, **kwargs):
        self.nums = []
        _input = kwargs.get('input', None) or [x.rstrip() for x in open('input.txt')]
        for line in _input:
            num = int(re.findall(r'\d+', line)[0])
            self.nums.append(num * (1 if line[0] == 'R' else -1))

    def solve(self):
        pos = 50
        ans = 0
        for num in self.nums:
            corr = abs(num) // 100
            ans += corr

            new_pos = pos + (num - corr * 100 if num > 0 else num + corr * 100)

            if num < 0 and new_pos <= 0 < pos: ans += 1
            if num > 0 and pos < 100 <= new_pos: ans += 1

            pos = new_pos % 100
        print(ans)
        return ans


if __name__ == '__main__':
    time = timeit(lambda: Day1().solve(), number=1)
    print(f'Execution time: {time:.4f}')
