from timeit import timeit


class Day1:
    ints = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.ints.append(int(line))

    def solve(self):
        previous = None
        increases = 0

        for i in range(len(self.ints) - 2):
            total = sum(self.ints[i:i + 3])
            if previous is not None:
                if total > previous:
                    increases += 1
            previous = total
        print(increases)


if __name__ == '__main__':
    time = timeit(lambda: Day1().solve(), number=1)
    print(f'Execution time: {time:.4f}')
