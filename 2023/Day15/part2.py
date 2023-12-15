def main():
    instructions = open('input.txt').readline().strip().split(',')
    boxes = []
    for instruction in instructions:
        if '=' in instruction:
            lens, strength = instruction.split('=')
            cur_box = get_box_num(lens)

            if cur_box not in boxes:
                for i in range(len(boxes), cur_box + 1, 1):
                    boxes.append({})

            boxes[cur_box][lens] = strength
        elif '-' in instruction:
            lens = instruction.replace('-', '')
            cur_box = next((i for i, box in enumerate(boxes) if lens in box.keys()), 0)
            if lens in boxes[cur_box]:
                del boxes[cur_box][lens]
    total = 0
    for i in range(len(boxes)):
        for j, (key, value) in enumerate(boxes[i].items()):
            total += (i + 1) * (j + 1) * int(value)
    print(total)


def get_box_num(label):
    hash_val = 0
    for char in label:
        hash_val += ord(char)
        hash_val *= 17
        hash_val %= 256
    return hash_val


if __name__ == '__main__':
    main()
