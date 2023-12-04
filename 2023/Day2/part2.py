import re
import math

minimums = {}
with open('input.txt') as f:
    for line in f:
        parts = line.split(': ')
        game_id = re.findall(r'\d+', parts[0])[0]
        minimums[game_id] = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        set_parts = re.findall(r'\d+ \w+', parts[1])
        for set_part in set_parts:
            split = set_part.split(' ')
            minimums[game_id][split[1]] = max(minimums[game_id][split[1]], int(split[0]))

total = 0
for game in minimums.values():
    total += math.prod(game.values())
print(total)
