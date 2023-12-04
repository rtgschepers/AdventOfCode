neighbours = []


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
            if value not in neighbours:
                neighbours.append(value)
            return True

    return


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
            if has_neighbouring_symbol(grid, x, y):
                symbol_adjacent = True

    flat = [x for y in valid_nums for x in y]
    print(sum(flat))


main()
print(neighbours)
