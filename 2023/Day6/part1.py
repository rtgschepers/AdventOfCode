import re

with open('input.txt') as f:
    numbers = [int(x) for x in re.findall(r'\d+', f.read())]
answer = 1
half_len = int(len(numbers) / 2)
for i in range(half_len):
    time = numbers[i]
    distance = numbers[i + half_len]
    possible_wins = 0
    for offset in range(1, time - 1):
        hold = offset
        travel = time - offset
        if hold * travel > distance:
            possible_wins += 1
    answer *= possible_wins
print(answer)
