import re

text_int_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def get_possible_matches(char):
    return [x for x in text_int_map.keys() if x and x[0] == char]


total = 0
with open('input.txt') as f:
    for line in f:
        numbers = []
        for i in range(len(line)):
            c = line[i]
            if c.isnumeric():
                numbers.append(c)
                continue

            matches = get_possible_matches(c)
            for match in matches:
                if line[i:i + len(match)] == match:
                    numbers.append(text_int_map[match])
                    break
        total += int(str(numbers[0]) + str(numbers[-1]))
print(total)
