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
free_space = 70000000 - dirs['/']
to_clean = 30000000 - free_space
print(min([v for v in dirs.values() if v >= to_clean]))
