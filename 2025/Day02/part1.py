from timeit import timeit


class Day2:
    data = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            for x in line.split(','):
                self.data.append([int(y) for y in x.split('-')])

    def solve(self):
        invalids = []
        for a, b in self.data:
            for x in range(a, b + 1):
                x = str(x)
                if len(x) % 2 != 0:
                    continue
                if x[:len(x)//2] == x[len(x)//2:]:
                    invalids.append(x)
        print(sum(int(x) for x in invalids))


if __name__ == '__main__':
    time = timeit(lambda: Day2().solve(), number=1)
    print(f'Execution time: {time:.4f}')
