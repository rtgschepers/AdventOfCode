import math

rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tail_path = [[0, 0]]


def move_head(axis, steps, direction):
    for i in range(steps):
        rope[0][axis] += 1 * direction
        if math.dist(rope[0], rope[1]) >= 2:
            move_rope(0, 1, axis, direction)

        if rope[len(rope) - 1] not in tail_path:
            tail_path.append(rope[len(rope) - 1].copy())


def move_rope(a, b, axis, direction):
    deg = angle_between(rope[a], rope[b])
    if math.dist(rope[a], rope[b]) > 2:
        rope[b][int(not axis)] += 1 * (1 if rope[a][int(not axis)] - rope[b][int(not axis)] else -1)
    rope[b][axis] += 1 * direction

    if b + 1 < len(rope) and math.dist(rope[a + 1], rope[b + 1]) >= 2:
        return move_rope(a + 1, b + 1, axis, direction)
    return


def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))


for line in [x.replace('\n', '') for x in open('test.txt')]:
    match line.split():
        case 'U', x:
            move_head(1, int(x), 1)
        case 'D', x:
            move_head(1, int(x), -1)
        case 'L', x:
            move_head(0, int(x), -1)
        case 'R', x:
            move_head(0, int(x), 1)
print(len(tail_path))
