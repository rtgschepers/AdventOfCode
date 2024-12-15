class Day7:
    def __init__(self):
        for line in [x.rstrip() for x in open('test.txt')]:
            pass

    def solve(self):
        pass


if __name__ == '__main__':
    Day7().solve()


    class Day7:


        signals = {}
    instructions = []
    max_int = 65535


    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            instruction, target = line.split(' -> ')
            self.parse_instruction(instruction, target)
            if target not in self.signals:
                self.signals[target] = None


    def parse_instruction(self, instruction, target):
        temp = {
            'signals': [],
            'operator': None,
            'target': target,
        }
        for part in instruction.split(' '):
            if not part.isnumeric() and part.upper() == part:
                temp['operator'] = part
            else:
                if part.isnumeric():
                    temp['signals'].append(int(part))
                else:
                    temp['signals'].append(part)
        self.instructions.append(temp)


    def solve(self):
        starts = [x for x in self.instructions if x['operator'] is None and x['target'] != 'a']
        self.execute_instructions(starts)
        print(self.signals['a'])


    def execute_instructions(self, instructions):
        for instruction in instructions:
            result = None
            match instruction['operator']:
                case None:
                    value = self.parse_value(instruction['signals'][0])
                    self.signals[instruction['target']] = value
                case 'AND':
                    left = self.parse_value(instruction['signals'][0])
                    right = self.parse_value(instruction['signals'][1])
                    result = left & right
                case 'OR':
                    result = self.signals[instruction['signals'][0]] | self.signals[instruction['signals'][1]]
                case 'LSHIFT':
                    result = self.signals[instruction['signals'][0]] << instruction['signals'][1]
                case 'RSHIFT':
                    result = self.signals[instruction['signals'][0]] >> instruction['signals'][1]
                case 'NOT':
                    self.signals[instruction['target']] = self.max_int - self.signals[instruction['signals'][0]]
            if result is not None:
                self.signals[instruction['target']] = result
            self.execute_instructions(self.get_next_instructions(instruction['target']))


    def parse_value(self, value):
        return value if isinstance(value, int) else self.signals[value]


    def get_next_instructions(self, target):
        return [x for x in self.instructions if target in x['signals'] and self.signals_have_values(x['signals'])]


    def signals_have_values(self, signals):
        for signal in signals:
            if not isinstance(signal, int) and self.signals[signal] is None:
                return False
        return True

if __name__ == '__main__':
    # Change the input line where 'b' gets a value to the answer of part 1
    Day7().solve()
