pos = {
    'x': 0,
    'y': 0
}
grid = {
    'x0y0': 0
}
for line in [x.rstrip() for x in open('input.txt')]:
    for char in line:
        if char == 'v':
            pos['y'] -= 1
        elif char == '^':
            pos['y'] += 1
        elif char == '<':
            pos['x'] -= 1
        elif char == '>':
            pos['x'] += 1
        key = 'x{}y{}'.format(pos['x'], pos['y'])
        if key not in grid:
            grid[key] = 1
        else:
            grid[key] += 1
print(len(grid.keys()))
