from timeit import timeit


class Day8:
    def __init__(self):
        for line in [x.rstrip() for x in open('test.txt')]:
            pass

    def solve(self):
        pass


if __name__ == '__main__':
    time = timeit(lambda: Day8().solve(), number=1)
    print(f'Execution time: {time:.4f}')
