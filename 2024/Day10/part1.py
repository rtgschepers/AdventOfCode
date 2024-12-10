import re
from collections import deque
from timeit import timeit


class Day10:
    topo = []
    starts = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self):
        for y, line in enumerate([x.rstrip() for x in open('input.txt')]):
            self.topo.append(line)
            for match in re.finditer(r'(0)', line):
                self.starts.append((match.start(), y))

    def solve(self):
        scores = []
        for start in self.starts:
            path = deque([start])
            score = 0
            while len(path):
                x, y = path.popleft()
                height = int(self.topo[y][x])

                if height == 9:
                    score += 1
                    continue

                for dx, dy in self.directions:
                    new_x, new_y = x + dx, y + dy
                    if not (0 <= new_y < len(self.topo) and 0 <= new_x < len(self.topo[0])):
                        continue

                    new_height = self.topo[new_y][new_x]
                    if new_height != '.' and int(new_height) == height + 1 and (new_x, new_y) not in path:
                        path.append((new_x, new_y))
            scores.append(score)
        print(scores)
        print(sum(scores))


if __name__ == '__main__':
    time = timeit(lambda: Day10().solve(), number=1)
    print(f'Execution time: {time:.4f}')
