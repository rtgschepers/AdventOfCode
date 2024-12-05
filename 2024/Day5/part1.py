import time


class Day5:
    rules = []
    updates = []

    def __init__(self):
        rules = True
        for line in [x.rstrip() for x in open('input.txt')]:
            if line == '':
                rules = False
                continue

            if rules:
                self.rules.append([int(x) for x in line.split('|')])
            else:
                self.updates.append([int(x) for x in line.split(',')])

    def solve(self):
        ans = 0
        for update in self.updates:
            correct = True
            for page in update:
                for rule in self.rules:
                    if page == rule[0]:
                        if rule[1] in update and update.index(page) > update.index(rule[1]):
                            correct = False
                            break
                    elif page == rule[1]:
                        if rule[0] in update and update.index(page) < update.index(rule[0]):
                            correct = False
                            break
            if correct:
                ans += update[len(update) // 2]
        print('Result: ', ans)


if __name__ == '__main__':
    start_time = time.time()
    Day5().solve()
    print('Execution time: ', str(time.time() - start_time))
