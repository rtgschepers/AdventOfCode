from collections import Counter
from timeit import timeit

from tqdm import tqdm


class Day11:
    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.stones = dict(Counter([int(x) for x in line.split(' ')]))

    def solve(self):
        seen_map = {}

        for _ in tqdm(range(75)):
            new_stones = {}
            for stone, count in self.stones.items():
                mutation = seen_map.setdefault(stone, self.mutate_value(stone))
                for m in mutation:
                    new_stones[m] = new_stones.get(m, 0) + count
            self.stones = new_stones
        print(sum(self.stones.values()))

    def mutate_value(self, n: int):
        if n == 0:
            return [1]
        elif len(str(n)) % 2 == 0:
            stone = str(n)
            return [int(stone[:len(stone) // 2]), int(stone[len(stone) // 2:])]
        else:
            return [n * 2024]


if __name__ == '__main__':
    time = timeit(lambda: Day11().solve(), number=1)
    print(f'Execution time: {time:.4f}')
