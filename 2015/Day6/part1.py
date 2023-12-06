import re

import numpy as np

grid = np.zeros((1000, 1000))
for line in [x.rstrip() for x in open('input.txt')]:
    instruction = re.findall(r'toggle|turn off|turn on', line)
    xy = [int(x) for x in re.findall(r'\d+', line)]
    if 'toggle' in instruction:
        grid[xy[0]:xy[2], xy[1]:xy[3]] = 1 - grid[xy[0]:xy[2], xy[1]:xy[3]]
    else:
        grid[xy[0]:xy[2], xy[1]:xy[3]] = 1 if 'on' in instruction else 0
print(np.count_nonzero(grid))
