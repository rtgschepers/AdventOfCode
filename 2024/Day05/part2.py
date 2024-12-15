from timeit import timeit


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
            unsorted = True
            updated = False
            while unsorted:
                unsorted = False
                for page in update:
                    for rule in self.rules:
                        if page in rule and rule[1 - rule.index(page)] in update:
                            if rule != [x for x in update if x in rule]:
                                unsorted = True
                                updated = True
                                update[update.index(rule[0])], update[update.index(rule[1])] = update[
                                    update.index(rule[1])], update[update.index(rule[0])]
            if updated:
                ans += update[len(update) // 2]
        print('Result: ', ans)


if __name__ == '__main__':
    time = timeit(lambda: Day5().solve(), number=1)
    print(f'Execution time: {time:.4f}')
