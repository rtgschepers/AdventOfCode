from hashlib import md5


class Day5:
    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.input = line

    def solve(self):
        password = ''
        counter = 3231928
        while True:
            counter += 1
            code = '{}{}'.format(self.input, counter)
            hex_val = md5(code.encode()).hexdigest()
            if hex_val[:5] == '00000':
                password += hex_val[5]
                if len(password) == 8:
                    break
        print(password)


if __name__ == '__main__':
    Day5().solve()
