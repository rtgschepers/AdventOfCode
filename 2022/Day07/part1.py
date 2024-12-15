from itertools import accumulate

path = []
dirs = {}

for line in [x.replace('\n', '') for x in open('input.txt')]:
    match line.split():
        case '$', 'cd', '..':
            path.pop()
        case '$', 'cd', x:
            path.append(x)
        case '$', 'ls':
            pass
        case 'dir', _:
            pass
        case size, _:
            temp = accumulate(path)
            for p in accumulate(path):
                if p in dirs:
                    dirs[p] += int(size)
                else:
                    dirs[p] = int(size)
print(sum([v for v in dirs.values() if v <= 100000]))
