import numpy as np


def get_tree_score(y, x, grid):
    cell = grid[y][x]
    directions = [grid[y][:x][::-1], grid[y][x + 1:], grid[:, x][:y][::-1], grid[:, x][y + 1:]]
    tree_score = 1
    for d in directions:
        tree_score *= next((i + 1 for i, v in enumerate(d) if v >= cell), len(d))
    return tree_score


forest = []
for line in [x.replace('\n', '') for x in open('input.txt')]:
    forest.append([int(x) for x in [*line]])
forest = np.array(forest)

max_score = 0
for y in range(1, len(forest) - 1):
    for x in range(1, len(forest[y]) - 1):
        max_score = max(max_score, get_tree_score(y, x, forest))

print(max_score)
