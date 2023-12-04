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

        if value is not None and value == '*':
            return str(new_x) + str(new_y)
    return None


def main():
    with open('input.txt') as f:
        grid = [x.rstrip() for x in f.readlines()]

    valid_nums = []
    number = ''
    symbol_adjacent = False
    symbol_position = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            cell = grid[y][x]
            if not cell.isnumeric():
                if symbol_adjacent:
                    valid_nums.append({'num': int(number), 'pos': symbol_position})

                symbol_adjacent = False
                number = ''
                continue

            number += cell
            position = has_neighbouring_symbol(grid, x, y)
            if position is not None:
                symbol_adjacent = True
                symbol_position = position

        if symbol_adjacent:
            valid_nums.append({'num': int(number), 'pos': symbol_position})

        symbol_adjacent = False
        number = ''

    total = 0
    get_value = lambda x: x['pos']
    positions = list({get_value(x): x for x in valid_nums})
    for position in positions:
        nums = [x['num'] for x in valid_nums if x['pos'] == position]
        if len(nums) == 2:
            total += nums[0] * nums[1]
    print(total)

main()
