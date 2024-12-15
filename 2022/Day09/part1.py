import math

head = [0, 0]
tail = [0, 0]
path = [[0, 0]]


def move_head(axis, steps, direction):
    for i in range(steps):
        head[axis] += 1 * direction
        if math.dist(head, tail) >= 2:
            move_tail(axis, direction)


def move_tail(axis, direction):
    if math.dist(head, tail) > 2:
        tail[int(not axis)] = head[int(not axis)]
    tail[axis] = head[axis] - (1 * direction)

    if tail not in path:
        path.append(tail.copy())


for line in [x.replace('\n', '') for x in open('test1.txt')]:
    match line.split():
        case 'U', x:
            move_head(1, int(x), 1)
        case 'D', x:
            move_head(1, int(x), -1)
        case 'L', x:
            move_head(0, int(x), -1)
        case 'R', x:
            move_head(0, int(x), 1)
print(len(path))
