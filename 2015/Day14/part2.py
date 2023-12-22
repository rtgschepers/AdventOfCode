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
            self.deer[name]['moving'] = int(limit)
            self.deer[name]['resting'] = 0
            self.deer[name]['distance'] = 0
            self.deer[name]['points'] = 0

    def solve(self):
        seconds = 2503
        for second in range(seconds):
            for deer, stats in self.deer.items():
                if stats['resting'] > 0:
                    stats['resting'] -= 1
                    if stats['resting'] == 0:
                        stats['moving'] = stats['limit']
                elif stats['moving'] > 0:
                    stats['moving'] -= 1
                    stats['distance'] += stats['speed']
                    if stats['moving'] == 0:
                        stats['resting'] = stats['rest']

            furthest = max([deer['distance'] for deer in self.deer.values()])
            leaders = [deer for deer, stats in self.deer.items() if stats['distance'] == furthest]
            for leader in leaders:
                self.deer[leader]['points'] += 1
        print(max([deer['points'] for deer in self.deer.values()]))
        pass

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
