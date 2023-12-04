def get_neighbours(grid, x, y):
    height = len(grid)
    width = len(grid[0])

    neighbours = []
    offsets = [{
        'direction': 'top-left',
        'offset': (-1, -1)
    }, {
        'direction': 'top',
        'offset': (-1, 0)
    }, {
        'direction': 'top-right',
        'offset': (-1, 1)
    }, {
        'direction': 'left',
        'offset': (0, -1)
    }, {
        'direction': 'right',
        'offset': (0, 1)
    }, {
        'direction': 'bottom-left',
        'offset': (1, -1)
    }, {
        'direction': 'bottom',
        'offset': (1, 0)
    }, {
        'direction': 'bottom-right',
        'offset': (1, 1)
    }]

    for offset in offsets:
        offset_x, offset_y = offset['offset']
        new_x, new_y = x + offset_x, y + offset_y

        try:
            if 0 <= new_x < width and 0 <= new_y < height:
                value = grid[new_y][new_x]
            else:
                value = None
        except IndexError:
            value = None

        neighbours.append({
            'direction': offset['direction'],
            'value': value
        })

    return neighbours


def main():
    with open('input.txt') as f:
        grid = [x.rstrip() for x in f.readlines()]

    valid_nums = []
    number = ''
    symbol_adjacent = False
    for y in range(len(grid)):
        valid_nums.append([])
        for x in range(len(grid[y])):
            cell = grid[y][x]
            if not cell.isnumeric():
                if symbol_adjacent:
                    valid_nums[y].append(int(number))

                symbol_adjacent = False
                number = ''
                continue

            number += cell
            neighbours = get_neighbours(grid, x, y)
            filtered = [x['value'] for x in neighbours if
                        x['value'] is not None and not x['value'].isnumeric() and x['value'] != '.']
            if len(filtered):
                symbol_adjacent = True

    flat = [x for y in valid_nums for x in y]
    print(sum(flat))


main()
