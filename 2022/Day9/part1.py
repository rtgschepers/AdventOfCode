def move_head(axis, steps):
    return()

head = [(0, 0)]
tail = [(0, 0)]
for line in [x.replace('\n', '') for x in open('test.txt')]:
    match line.split():
        case 'U', x: head.append(move_head(head[len(head) - 1][1], x))
        case 'D', x: head.append(move_head(head[len(head) - 1][1], x * -1))
        case 'L', x: head.append(move_head(head[len(head) - 1][0], x * -1))
        case 'R', x: head.append(move_head(head[len(head) - 1][0], x))
print(head)
