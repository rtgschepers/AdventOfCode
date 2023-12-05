import re

with open('input.txt') as f:
    content = f.read()

sections = content.split('\n\n')
seeds = [int(x) for x in re.findall(r'\d+', sections[0])]
answer = 999999999

for seed in seeds:
    value = seed
    for section in sections[1:]:
        maps = [[int(y) for y in x.split(' ')] for x in section.split('\n')[1:]]
        for destination, source, map_range in maps:
            if source <= value < source + map_range:
                value += destination - source
                break
    answer = min(answer, value)
print(answer)
