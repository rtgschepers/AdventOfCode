maps = {}
with open('input.txt') as f:
    instructions = f.readline().strip()
    f.readline()

    for line in f.readlines():
        parts = line.strip().split(' = ')
        lr = parts[1].replace('(', '').replace(')', '').split(', ')
        maps[parts[0]] = {
            'L': lr[0],
            'R': lr[1],
        }

cur_pos = 'AAA'
steps = 0
while cur_pos != 'ZZZ':
    step = instructions[steps % len(instructions)]
    cur_pos = maps[cur_pos][step]
    steps += 1
print(steps)
