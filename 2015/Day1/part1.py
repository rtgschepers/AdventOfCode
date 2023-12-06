import re

for line in [x.rstrip() for x in open('input.txt')]:
    up = len(re.findall(r'\(', line))
    down = len(line) - up
    print(up - down)
