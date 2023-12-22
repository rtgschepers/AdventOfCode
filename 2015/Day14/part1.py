import re


class Day14:
    deer = {}

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            name = re.findall(r'^\w+', line)[0]
            if name not in self.deer:
                self.deer[name] = {}

            speed, limit, rest = re.findall(r'\d+', line)
            self.deer[name]['speed'] = int(speed)
            self.deer[name]['limit'] = int(limit)
            self.deer[name]['rest'] = int(rest)

    def solve(self):
        seconds = 2503
        distances = []
        for deer, stats in self.deer.items():
            distances.append(self.calc_distance(stats, seconds))
        print(max(distances))

    def calc_distance(self, stats, seconds):
        distance = 0
        speed, limit, rest = stats.values()
        while seconds >= limit:
            seconds -= limit
            distance += speed * limit
            seconds -= rest

        if seconds > 0:
            distance += speed * seconds

        return distance


if __name__ == '__main__':
    Day14().solve()
