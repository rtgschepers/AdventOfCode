import re
from timeit import timeit


class Day13:
    machines = []
    conversion = 10000000000000

    def __init__(self):
        temp = ''
        for line in [x.rstrip() for x in open('input.txt')]:
            temp += line
            if line == '':
                self.machines.append([int(x) for x in re.findall(r'\d+', temp)])
                temp = ''
        self.machines.append([int(x) for x in re.findall(r'\d+', temp)])

    def solve(self):
        total = 0
        for machine in self.machines:
            x = self.calc_x(machine)
            if x is not None:
                y = self.calc_y(machine, x)
                total += x * 3 + y
        print(total)

    def calc_x(self, machine) -> None | int:
        x1, y1, x2, y2, x3, y3 = machine
        x3, y3 = x3 + self.conversion, y3 + self.conversion

        left = y2 * x3 - x2 * y3
        right = y2 * x1 - x2 * y1
        return left // right if left % right == 0 else None

    def calc_y(self, machine, x) -> int:
        x1, y1, x2, y2, x3, y3 = machine
        x3, y3 = x3 + self.conversion, y3 + self.conversion
        return (x3 - x1 * x) // x2


if __name__ == '__main__':
    time = timeit(lambda: Day13().solve(), number=1)
    print(f'Execution time: {time:.4f}')
