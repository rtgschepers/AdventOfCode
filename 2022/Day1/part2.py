f = open('test.txt')
top3 = [0, 0, 0]
current = 0


def update_top3(top3, new_val):
    low = min(top3)
    top3[top3.index(low)] = max(new_val, low)
    return top3


lines = f.readlines()
for line in lines:
    if line == '\n':
        top3 = update_top3(top3, current)
        current = 0
    else:
        current += int(line)
        if line == lines[len(lines) - 1]:
            top3 = update_top3(top3, current)
print(sum(top3))
