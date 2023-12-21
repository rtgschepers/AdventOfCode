class Day10:
    lines = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.lines.append(line)
            pass

    def solve(self):
        line = self.lines[0]
        for i in range(50):
            output = ''
            cur_count = 0
            last_char = line[0]
            for char in line:
                if char != last_char:
                    output += str(cur_count) + last_char
                    cur_count = 0
                cur_count += 1
                last_char = char
            output += str(cur_count) + last_char
            line = output
        print(len(line))


if __name__ == '__main__':
    Day10().solve()
