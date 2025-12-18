import math
import re
from timeit import timeit


class Day17:
    registers = {}

    def __init__(self):
        registers = True
        for line in [x.rstrip() for x in open('input.txt')]:
            if line == '':
                registers = False
                continue

            if registers:
                match = re.findall(r'(\w): (\d+)', line)[0]
                self.registers[match[0]] = int(match[1])
            else:
                self.program = [int(x) for x in re.findall(r'\d+', line)]

    def solve(self):
        i = 0
        outputs = []

        while i < len(self.program):
            opcode = self.program[i]
            operand = self.program[i + 1]

            match opcode:
                case 0:
                    self.registers['A'] = math.trunc(self.registers['A'] / pow(2, self.get_combo_operand(operand)))
                case 1:
                    self.registers['B'] = self.registers['B'] ^ operand
                case 2:
                    self.registers['B'] = self.get_combo_operand(operand) % 8
                case 3:
                    if self.registers['A'] != 0:
                        i = operand
                        continue
                case 4:
                    self.registers['B'] = self.registers['B'] ^ self.registers['C']
                case 5:
                    outputs.append(str(self.get_combo_operand(operand) % 8))
                case 6:
                    self.registers['B'] = math.trunc(self.registers['A'] / pow(2, self.get_combo_operand(operand)))
                case 7:
                    self.registers['C'] = math.trunc(self.registers['A'] / pow(2, self.get_combo_operand(operand)))

            i += 2
        print(','.join(outputs))

    def get_combo_operand(self, operand: int) -> int:
        if operand < 4:
            return operand
        if operand == 4:
            return self.registers['A']
        if operand == 5:
            return self.registers['B']
        if operand == 6:
            return self.registers['C']
        if operand == 7:
            print('Invalid program:', self.program)
            exit(1)


if __name__ == '__main__':
    time = timeit(lambda: Day17().solve(), number=1)
    print(f'Execution time: {time:.4f}')
