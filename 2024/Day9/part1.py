from timeit import timeit


class Day9:
    offset = 48
    _input = str

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self._input = line + '0' if len(line) % 2 else line

    def solve(self):
        blocks = ''
        for i in range(0, len(self._input), 2):
            blocks += chr(i // 2 + self.offset) * int(self._input[i])
            blocks += '.' * int(self._input[i + 1])

        while blocks.count('.'):
            if blocks[-1] == '.':
                blocks = blocks[:-1]
                continue

            i = blocks.index('.')
            blocks = blocks[:i] + blocks[-1] + blocks[i + 1:-1]

        total = 0
        for i in range(len(blocks)):
            total += i * (ord(blocks[i]) - self.offset)
        print(total)


if __name__ == '__main__':
    time = timeit(lambda: Day9().solve(), number=1)
    print(f'Execution time: {time:.4f}')
