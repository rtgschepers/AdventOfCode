import re

bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
total = 0
with open('input.txt') as f:
    for line in f:
        parts = line.split(': ')
        game_id = re.findall(r'\d+', parts[0])[0]
        set_parts = re.findall(r'\d+ \w+', parts[1])

        possible = True
        for set_part in set_parts:
            split = set_part.split(' ')
            if int(split[0]) > bag[split[1]]:
                possible = False
                break

        if possible:
            total += int(game_id)
print(total)
