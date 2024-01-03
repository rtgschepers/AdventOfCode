class Day20:
    target = 0
    houses = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.target = int(line)

    def solve(self):
        house = 1
        while True:
            gifts = 0
            divisors = self.get_divisors(house)
            for elf in divisors:
                gifts += elf * 1

            if gifts >= self.target:
                print(house)
                exit()
            house += 1

    def get_divisors(self, number):
        divisors = [1]
        sqrt_number = int(number ** 0.5) + 1
        for i in range(2, sqrt_number):
            if number % i == 0:
                divisors.append(i)
                if i != number // i:
                    divisors.append(number // i)
        if number not in divisors:
            divisors.append(number)
        return divisors


if __name__ == '__main__':
    Day20().solve()
