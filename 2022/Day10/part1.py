def main():
    total = 0
    cycle = 0
    x = 1
    for line in [x.rstrip() for x in open('input.txt')]:
        if 'noop' in line:
            cycle += 1
            if is_key_cycle(cycle):
                total += cycle * x
        elif 'addx' in line:
            cycle += 1
            if is_key_cycle(cycle):
                total += cycle * x
            cycle += 1
            if is_key_cycle(cycle):
                total += cycle * x
            value = int(line.split(' ')[1])
            x += value
    print(total)


def is_key_cycle(cycle):
    if (cycle - 20) % 40 == 0:
        return True
    return False


if __name__ == '__main__':
    main()
