tree = {}
path = ''
for line in [x.replace('\n', '') for x in open('input.txt')]:
    command = line.split(' ')
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] == '..':
                path = path[:-1]
            else:
                path += command[2]
                tree[path] = {
                    'type': 'dir',
                }
        if command[1] == 'ls':
            # add dirs and files to tree
            continue
        continue
    if command[0].isnumeric():
        tree[path + command[1]] = {
            'type': 'file',
            'size': int(command[0])
        }

total = 0
dirs = [k for k, v in tree.items() if v['type'] == 'dir']
# Adds dirs to tree on LS command. Not all dirs have files, but can have dirs with files.
for dir in dirs:
    in_dir = [v['size'] for k, v in tree.items() if k.startswith(dir) and v['type'] != 'dir']
    dir_size = sum(in_dir)
    total += dir_size if dir_size <= 100000 else 0
print(total)
