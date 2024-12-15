from hashlib import md5


class Day5:
    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.input = line

    def solve(self):
        password = [None] * 8
        counter = 3231928
        while True:
            counter += 1
            code = '{}{}'.format(self.input, counter)
            hex_val = md5(code.encode()).hexdigest()
            if hex_val[:5] == '00000':
                if not hex_val[5].isnumeric():
                    continue

                key = int(hex_val[5])
                if key >= len(password):
                    continue

                if password[key] is None:
                    password[key] = hex_val[6]

                if None not in password:
                    break
        print(''.join(password))


if __name__ == '__main__':
    Day5().solve()
