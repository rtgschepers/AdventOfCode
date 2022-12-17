import re

sum = 0
file = open('input.txt', 'r')
lines = [x.replace('\n', '') for x in file.readlines()]
for i in range(0, len(lines), 3):
    duplicate = list(set(lines[i]).intersection(set(lines[i + 1])).intersection(set(lines[i + 2])))[0]
    correction = 38 if re.match('^[a-z]$', duplicate) is None else 96
    sum += ord(duplicate) - correction
print(sum)
