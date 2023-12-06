import re

with open('input.txt') as f:
    numbers = [int(x) for x in re.findall(r'\d+', f.read())]
answer = 1
for i in range(len(numbers) // 2):
    time = numbers[i]
    distance = numbers[i + len(numbers) // 2]
    for offset in range(1, time - 1):
        hold = offset
        travel = time - offset
        if hold * travel > distance:
            answer *= time - (offset * 2 - 1)
            break
print(answer)
