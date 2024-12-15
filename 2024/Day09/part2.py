from timeit import timeit


class Day9:
    offset = 48
    _input = str

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self._input = line + '0' if len(line) % 2 else line

    def solve(self):
        files = []
        blocks = ''
        for i in range(0, len(self._input), 2):
            file = str(chr(i // 2 + self.offset) * int(self._input[i]))
            files.append(file)
            blocks += file
            blocks += '.' * int(self._input[i + 1])
        files.reverse()

        for file in files[:-1]:
            try:
                i = blocks.index('.' * len(file))
                if i < blocks.index(file):
                    blocks = blocks.replace(file, '.' * len(file))
                    blocks = blocks[:i] + file + blocks[i + len(file):]
            except ValueError:
                pass

        total = 0
        for i in range(len(blocks)):
            if blocks[i] != '.':
                total += i * (ord(blocks[i]) - self.offset)
        print(total)


if __name__ == '__main__':
    time = timeit(lambda: Day9().solve(), number=1)
    print(f'Execution time: {time:.4f}')
