import re

with open('input.txt') as f:
    numbers = [x for x in re.findall(r'\d+', f.read())]
half_len = int(len(numbers) / 2)
time = int(''.join(numbers[:half_len]))
distance = int(''.join(numbers[half_len:]))
possible_wins = 0
for offset in range(1, time - 1):
    hold = offset
    travel = time - offset
    if hold * travel > distance:
        possible_wins += 1
print(possible_wins)
