cycle = 0
x = 1
key_cycles = [20, 60, 100, 140, 180, 220]


def print_answer():
    print('cycle: {} - x: {}'.format(cycle, x))


def increase_cycle():
    cycle = cycle + 1
    print_answer()


for line in [x.rstrip() for x in open('test.txt')]:
    cycle += 1
    parts = line.split(' ')

    print_answer()

    if parts[0] == 'addx':
        cycle += 1
        x += int(parts[1])
        print_answer()

print_answer()
