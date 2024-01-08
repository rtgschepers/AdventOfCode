import re


class Day23:
    registers = {
        'a': 1,
        'b': 0
    }
    instructions = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.instructions.append(re.findall(r'[+-]*\w+', line))
            pass

    def solve(self):
        i = 0
        while i < len(self.instructions):
            instruction = self.instructions[i]
            match instruction[0]:
                case 'hlf':
                    self.registers[instruction[1]] //= 2
                case 'tpl':
                    self.registers[instruction[1]] *= 3
                case 'inc':
                    self.registers[instruction[1]] += 1
                case 'jmp':
                    i += int(instruction[1]) - 1
                case 'jie':
                    if self.registers[instruction[1]] % 2 == 0:
                        i += int(instruction[2]) - 1
                case 'jio':
                    if self.registers[instruction[1]] == 1:
                        i += int(instruction[2]) - 1
            i += 1
        print(self.registers)


if __name__ == '__main__':
    Day23().solve()
