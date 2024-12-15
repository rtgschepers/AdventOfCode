count = 0
file = open('input.txt', 'r')
for line in [x.replace('\n', '') for x in file.readlines()]:
    parts = [[y for y in range(int(x.split('-')[0]), int(x.split('-')[1]) + 1)] for x in line.split(',')]
    intersection = set(parts[0]).intersection(parts[1])
    if len(list(intersection)) > 0:
        count += 1
print(count)
