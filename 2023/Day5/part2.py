import re
import sys

import numpy as np

with open('input.txt') as f:
    content = f.read()

sections = content.split('\n\n')
seeds = [int(x) for x in re.findall(r'\d+', sections[0])]
seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
answer = sys.maxsize

for seed, seed_range in seeds:
    print(seed, seed_range)
    seed_vals = np.arange(seed, seed + seed_range)
    cur_seeds = np.column_stack((seed_vals, np.zeros_like(seed_vals))).reshape((len(seed_vals), 2), order='F')

    for section in sections[1:]:
        print(section.split('\n')[0])
        lowest = np.min(cur_seeds[:, 0])
        highest = np.max(cur_seeds[:, 0])

        for destination, source, map_range in [[int(y) for y in x.split(' ')] for x in section.split('\n')[1:]]:
            if highest < source or lowest >= source + map_range:
                continue

            mask = (source <= cur_seeds[:, 0]) & (cur_seeds[:, 0] < source + map_range) & (cur_seeds[:, 1] == 0)
            cur_seeds[mask, 0] += destination - source
            cur_seeds[mask, 1] = 1

            if np.count_nonzero(cur_seeds[:, 1] == 1) == len(cur_seeds):
                break
        cur_seeds[:, 1] = 0
    lowest = np.min(cur_seeds[:, 0])
    answer = min(answer, lowest)
print(answer)
