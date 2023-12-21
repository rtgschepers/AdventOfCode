class Day11:
    password = None

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.password = [ord(x) for x in line]

    def solve(self):
        while True:
            self.increment()
            if self.has_three_sequential() and self.has_two_pairs():
                break

        print(''.join([chr(x) for x in self.password]))

    def increment(self):
        i = len(self.password) - 1

        while True:
            next_char = self.get_next_char(self.password[i])
            self.password[i] = next_char
            if next_char != 97:  # unicode for 'a'
                break
            i -= 1

    def get_next_char(self, char):
        code = char + 1
        while code in [105, 108, 111]:  # skip 'i', 'l', 'o'
            code += 1

        if code > 122:  # unicode for 'z'
            code -= 26  # length of alphabet; back to 'a'
        return code

    def has_three_sequential(self):
        return any(self.password[i] + 1 == self.password[i + 1] == self.password[i + 2] - 1 for i in range(len(self.password) - 2))

    def has_two_pairs(self):
        return len(set((self.password[i], self.password[i + 1]) for i in range(len(self.password) - 1) if self.password[i] == self.password[i + 1])) >= 2


if __name__ == '__main__':
    Day11().solve()
