def main():
    hands = []
    for line in [x.rstrip() for x in open('input.txt')]:
        parts = line.split(' ')
        hand = {
            'hand': parts[0],
            'bet': int(parts[1]),
            'type': get_type(parts[0])
        }
        hands.append(hand)

    order = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    hands = sorted(hands, key=lambda x: (x['type'], [order[c] for c in x['hand']]), reverse=True)

    total = 0
    for i, hand in enumerate(hands):
        total += hand['bet'] * (i + 1)
    print(total)


def get_type(hand):
    functions = [
        'is_five_of_a_kind',
        'is_four_of_a_kind',
        'is_full_house',
        'is_three_of_a_kind',
        'is_two_pair',
        'is_pair',
    ]
    for i in range(len(functions)):
        if globals()[functions[i]](hand):
            return i
    return len(functions)


def is_five_of_a_kind(string):
    return len(set(string)) == 1


def is_four_of_a_kind(string):
    chars = set(string)
    if len(chars) == 2:
        for char in chars:
            if string.count(char) == 4:
                return True
    return False


def is_full_house(string):
    chars = list(set(string))
    if len(chars) == 2:
        counts = [string.count(chars[0]), string.count(chars[1])]
        if 2 in counts and 3 in counts:
            return True
    return False


def is_three_of_a_kind(string):
    chars = set(string)
    if 1 < len(chars) < 4:
        for char in chars:
            if string.count(char) == 3:
                return True
    return False


def is_two_pair(string):
    chars = list(set(string))
    if len(chars) == 3:
        counts = [string.count(chars[0]), string.count(chars[1]), string.count(chars[2])]
        if counts.count(2):
            return True
    return False


def is_pair(string):
    chars = set(string)
    for char in chars:
        if string.count(char) == 2:
            return True
    return False


if __name__ == '__main__':
    main()
