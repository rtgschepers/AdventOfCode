floor = 0
for line in [x.rstrip() for x in open('input.txt')]:
    for x in range(len(line)):
        floor += 1 if line[x] == '(' else -1
        if floor == -1:
            print(x + 1)
            break
