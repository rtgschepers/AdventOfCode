def main():
    pipes = {
        '|': ['n', 's'],
        '-': ['e', 'w'],
        'L': ['n', 'e'],
        'J': ['n', 'w'],
        '7': ['s', 'w'],
        'F': ['s', 'e'],
        '.': [],
        'S': [],
    }
    tiles = []
    for line in [x.rstrip() for x in open('input.txt')]:
        tiles.append(list(line))

    x, y = find_start(tiles)
    pipes['S'] = determine_start_connections(pipes, tiles, x, y)
    direction = get_opposite_direction(pipes['S'][0])
    path = []

    while True:
        opposite_direction = get_opposite_direction(direction)
        direction = pipes[tiles[y][x]][1 - pipes[tiles[y][x]].index(opposite_direction)]
        x, y = get_new_position(x, y, direction)
        path.append((x, y))
        if tiles[y][x] == 'S':
            break
    print(len(path) / 2)


def find_start(tiles):
    for i, x in enumerate(tiles):
        if 'S' in x:
            return x.index('S'), i


def determine_start_connections(pipes, tiles, x, y):
    connections = []
    if 's' in pipes[tiles[y - 1][x]]:
        connections.append('n')
    if 'n' in pipes[tiles[y + 1][x]]:
        connections.append('s')
    if 'e' in pipes[tiles[y][x - 1]]:
        connections.append('w')
    if 'w' in pipes[tiles[y][x + 1]]:
        connections.append('e')
    return connections


def get_opposite_direction(direction):
    if direction == 's':
        return 'n'
    if direction == 'n':
        return 's'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'


def get_new_position(x, y, direction):
    if direction == 'n':
        return x, y - 1
    if direction == 's':
        return x, y + 1
    if direction == 'e':
        return x + 1, y
    if direction == 'w':
        return x - 1, y


if __name__ == '__main__':
    main()
