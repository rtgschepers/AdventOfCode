class Day8:
    code_len = []
    mem_len = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            temp = repr(line)
            self.code_len.append(len(temp) + temp.count("\""))
            self.mem_len.append(len(line))

    def solve(self):
        print(sum(self.code_len) - sum(self.mem_len))


if __name__ == '__main__':
    Day8().solve()
