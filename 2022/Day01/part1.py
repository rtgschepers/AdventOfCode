f = open('test.txt')
highest = 0
current = 0

for line in f.readlines():
    if line == '\n':
        highest = max(current, highest)
        current = 0
    else:
        current += int(line)
print(highest)
