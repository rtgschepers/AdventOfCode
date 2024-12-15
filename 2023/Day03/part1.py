def has_neighbouring_symbol(grid, x, y):
    height = len(grid)
    width = len(grid[0])

    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for offset_x, offset_y in offsets:
        new_x, new_y = x + offset_x, y + offset_y

        try:
            if 0 <= new_x < width and 0 <= new_y < height:
                value = grid[new_y][new_x]
            else:
                value = None
        except IndexError:
            value = None

        if value is not None and not value.isnumeric() and value != '.':
            return True
    return


def main():
    with open('input.txt') as f:
        grid = [x.rstrip() for x in f.readlines()]

    total = 0
    number = ''
    symbol_adjacent = False
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            cell = grid[y][x]
            if not cell.isnumeric():
                if symbol_adjacent:
                    total += int(number)
                symbol_adjacent = False
                number = ''
                continue
            number += cell
            if has_neighbouring_symbol(grid, x, y):
                symbol_adjacent = True
        if symbol_adjacent:
            total += int(number)
        symbol_adjacent = False
        number = ''
    print(total)


main()
