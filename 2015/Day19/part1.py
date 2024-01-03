class Day19:
    operations = []
    molecule = ''
    molecules = []

    def __init__(self):
        lines = [x.rstrip() for x in open('input.txt')]
        for line in lines:
            if line == '':
                break

            self.operations.append(line.split(' => '))
        self.molecule = lines[-1]

    def solve(self):
        for operation in self.operations:
            src, trg = operation
            indices = [index for index in range(len(self.molecule)) if self.molecule.startswith(src, index)]
            pass
            for index in indices:
                molecule = self.molecule[:index] + trg + self.molecule[index + len(src):]
                if molecule not in self.molecules:
                    self.molecules.append(molecule)
        print(len(self.molecules))


if __name__ == '__main__':
    Day19().solve()
