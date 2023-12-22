import json


class Day12:
    structure = None
    score = 0

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.structure = json.loads(line)

    def solve(self):
        self.loop(self.structure)
        print(self.score)

    def loop(self, dict_list):
        for x in dict_list:
            if isinstance(x, dict):
                self.recur_dict(x)
            elif isinstance(x, list):
                self.recur_list(x)
            elif isinstance(x, int):
                self.score += x

    def recur_dict(self, _dict):
        if 'red' in _dict.values():
            return
        self.loop(_dict.values())

    def recur_list(self, _list):
        self.loop(_list)


if __name__ == '__main__':
    Day12().solve()
