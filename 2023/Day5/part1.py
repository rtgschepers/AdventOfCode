import math
import re

total = 0
with open('input.txt') as f:
    for line in f:
        numbers = line.split(': ')[1].split(' | ')
        win_nums = re.findall(r'\d+', numbers[0])
        my_nums = re.findall(r'\d+', numbers[1])
        my_win_nums = [x for x in my_nums if x in win_nums]

        if len(my_win_nums) == 1:
            total += 1
        elif len(my_win_nums) > 1:
            total += math.pow(2, len(my_win_nums) - 1)
print(total)
