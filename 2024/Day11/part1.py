from timeit import timeit


class Day11:
    stones = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.stones = [int(x) for x in line.split(' ')]

    def solve(self):
        for _ in range(25):
            mute = []
            for stone in self.stones:
                if stone == 0:
                    mute.append(1)
                elif len(str(stone)) % 2 == 0:
                    stone = str(stone)
                    mute.append(int(stone[:len(stone) // 2]))
                    mute.append(int(stone[len(stone) // 2:]))
                else:
                    mute.append(stone * 2024)
            self.stones = mute
        print(len(self.stones))


if __name__ == '__main__':
    time = timeit(lambda: Day11().solve(), number=1)
    print(f'Execution time: {time:.4f}')
