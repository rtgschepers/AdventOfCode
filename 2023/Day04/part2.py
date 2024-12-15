import re

card_amounts = {}


def add_card_amount(card):
    if card not in card_amounts:
        card_amounts[card] = 1
    else:
        card_amounts[card] += 1


with open('input.txt') as f:
    for line in f:
        card_num = int(re.search(r'(\d+)', line).group())
        add_card_amount(card_num)

        numbers = line.split(': ')[1].split(' | ')
        win_nums = re.findall(r'\d+', numbers[0])
        my_nums = re.findall(r'\d+', numbers[1])
        my_win_nums = [x for x in my_nums if x in win_nums]

        for x in range(card_amounts[card_num]):
            for y in range(len(my_win_nums)):
                add_card_amount(card_num + (y + 1))
print(sum(card_amounts.values()))
