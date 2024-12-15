import re

import numpy as np

grid = np.zeros((1000, 1000))
for line in [x.rstrip() for x in open('input.txt')]:
    instruction = re.findall(r'toggle|turn off|turn on', line)[0]
    x1, y1, x2, y2 = [int(x) for x in re.findall(r'\d+', line)]
    x2, y2 = x2 + 1, y2 + 1
    if 'toggle' in instruction:
        grid[y1:y2, x1:x2] += 2
    elif 'on' in instruction:
        grid[y1:y2, x1:x2] += 1
    else:
        mask = grid[y1:y2, x1:x2] > 0
        grid[y1:y2, x1:x2][mask] -= 1
print(np.sum(grid))
