def check_fully_contains(a, b):
    return a[0] >= b[0] and a[1] <= b[1]


count = 0
file = open('input.txt', 'r')
for line in [x.replace('\n', '') for x in file.readlines()]:
    parts = [[int(y) for y in x.split('-')] for x in line.split(',')]
    if check_fully_contains(parts[0], parts[1]) or check_fully_contains(parts[1], parts[0]):
        count += 1
print(count)
