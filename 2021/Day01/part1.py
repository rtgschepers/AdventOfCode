from timeit import timeit


class Day1:
    previous = None
    increases = 0

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            val = int(line)
            if self.previous is not None:
                if val > self.previous:
                    self.increases += 1
            self.previous = val

    def solve(self):
        print(self.increases)


if __name__ == '__main__':
    time = timeit(lambda: Day1().solve(), number=1)
    print(f'Execution time: {time:.4f}')
