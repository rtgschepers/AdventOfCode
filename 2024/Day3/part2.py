import re
import time


class Day3:
    instructions = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.instructions += [[y for y in x if y != ''] for x in re.findall(r'(don\'t)\(\)|(do)\(\)|(mul)\((\d+),(\d+)\)', line)]

    def solve(self):
        do_mul = True
        ans = 0

        for x in self.instructions:
            match x[0]:
                case 'don\'t':
                    do_mul = False
                case 'do':
                    do_mul = True
                case 'mul':
                    if do_mul:
                        ans += int(x[1]) * int(x[2])
        print(ans)


if __name__ == '__main__':
    start_time = time.time()
    Day3().solve()
    print('Execution time: ' + str(time.time() - start_time))
