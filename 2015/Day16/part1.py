import re


class Day16:
    sue = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    aunts = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            properties = re.findall(r'[A-z]+', line)
            values = re.findall(r'-*\d+', line)

            self.aunts.append({})
            for i in range(1, len(properties)):
                self.aunts[-1][properties[i]] = int(values[i])

    def solve(self):
        for i in range(len(self.aunts)):
            if self.is_match(self.aunts[i]):
                print(i + 1)

    def is_match(self, aunt):
        for key, val in aunt.items():
            if self.sue[key] != val:
                return False
        return True


if __name__ == '__main__':
    Day16().solve()
