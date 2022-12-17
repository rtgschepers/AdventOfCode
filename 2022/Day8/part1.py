import numpy as np


def is_visible(y, x, grid):
    cell = grid[y][x]
    if cell > max(grid[y][:x]):  # left
        return True
    if cell > max(grid[y][x + 1:]):  # right
        return True
    if cell > max(grid[:, x][:y]):  # up
        return True
    if cell > max(grid[:, x][y + 1:]):  # down
        return True
    return False


forest = []
for line in [x.replace('\n', '') for x in open('input.txt')]:
    forest.append([int(x) for x in [*line]])
forest = np.array(forest)

visible = (len(forest) - 1) * 4
for y in range(1, len(forest) - 1):
    for x in range(1, len(forest[y]) - 1):
        if is_visible(y, x, forest):
            visible += 1

print(visible)
