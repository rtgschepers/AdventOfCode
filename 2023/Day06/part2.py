import re

with open('input.txt') as f:
    numbers = [x for x in re.findall(r'\d+', f.read())]

time = int(''.join(numbers[:len(numbers) // 2]))
distance = int(''.join(numbers[len(numbers) // 2:]))

for offset in range(0, time, 1):
    hold = offset
    travel = time - offset
    if hold * travel > distance:
        print(time - (offset * 2 - 1))
        break
