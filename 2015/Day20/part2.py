class Day20:
    target = 0
    divisors = []
    all_divisors = {}

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.target = int(line)

    def solve(self):
        house = 1
        while True:
            gifts = 0
            self.fill_divisors(house)
            for elf in self.divisors:
                gifts += elf * 11

            if gifts >= self.target:
                print(house)
                exit()
            house += 1

    def fill_divisors(self, number):
        self.divisors = []
        self.add_and_increment(1)

        sqrt_number = int(number ** 0.5) + 1
        for i in range(2, sqrt_number):
            if number % i == 0:
                self.add_and_increment(i)
                if i != number // i:
                    self.add_and_increment(number // i)
        if number not in self.divisors:
            self.add_and_increment(number)

    def add_and_increment(self, divisor):
        if divisor not in self.all_divisors:
            self.all_divisors[divisor] = 0

        if self.all_divisors[divisor] < 50:
            self.divisors.append(divisor)
            self.all_divisors[divisor] += 1


if __name__ == '__main__':
    Day20().solve()
