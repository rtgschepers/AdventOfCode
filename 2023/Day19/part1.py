import re


class Day19:
    accepted = []
    rejected = []
    workflows = {}
    parts = []

    def __init__(self):
        lines = [x.strip() for x in open('input.txt').readlines()]
        start = 0
        for i in range(len(lines)):
            if lines[i] == '':
                start = i + 1
                break
            key, workflow = lines[i].split('{')
            self.workflows[key] = [x.split(':') for x in workflow[:-1].split(',')]
        for i in range(start, len(lines)):
            self.parts.append(tuple([int(x) for x in re.findall(r'\d+', lines[i])]))

    def solve(self):
        answer = 0
        for part in self.parts:
            self.handle_workflow('in', part)
        for tup in self.accepted:
            answer += sum(tup)
        print(answer)

    def handle_workflow(self, workflow, part):
        x, m, a, s = part
        for rule in self.workflows[workflow]:
            if len(rule) == 2:
                if eval(rule[0]):
                    return self.process_result(rule[1], part)
            else:
                return self.process_result(rule[0], part)

    def process_result(self, rule, part):
        if rule == 'R':
            return self.rejected.append(part)
        elif rule == 'A':
            return self.accepted.append(part)
        else:
            return self.handle_workflow(rule, part)


if __name__ == '__main__':
    Day19().solve()
