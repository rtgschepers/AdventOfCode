import re

total = 0
for line in [x.rstrip() for x in open('input.txt')]:
    l, w, h = [int(x) for x in re.findall(r'\d+', line)]
    total += 2 * (l * w + w * h + l * h) + min(l * w, w * h, h * l)
print(total)
