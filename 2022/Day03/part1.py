import re

sum = 0
file = open('input.txt', 'r')
for line in [x.replace('\n', '') for x in file.readlines()]:
    part1 = [*line[:len(line) // 2]]
    part2 = [*line[len(line) // 2:]]
    duplicate = list(set(part1).intersection(part2))[0]
    correction = 38 if re.match('^[a-z]$', duplicate) is None else 96
    sum += ord(duplicate) - correction
print(sum)
