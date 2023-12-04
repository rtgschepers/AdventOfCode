import re

total = 0
with open('input.txt') as f:
    for line in f:
        numbers = re.findall(r'[0-9]', line)
        total += int(str(numbers[0]) + str(numbers[-1]))
print(total)
