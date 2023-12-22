import re


class Day13:
    guests = {}
    arrangements = []

    def __init__(self):
        for line in [x.rstrip()[:-1] for x in open('input.txt')]:
            value = int(re.findall(r'\d+', line)[0])
            value *= -1 if 'lose' in line else 1

            name = re.findall(r'^\w+', line)[0]
            neighbour = re.findall(r'\w+$', line)[0]

            if name not in self.guests:
                self.guests[name] = {}
            self.guests[name][neighbour] = value

    def solve(self):
        self.add_me()
        for guests in self.guests:
            self.recur_arrangement([guests])

        max_happiness = 0
        for arrangement in self.arrangements:
            happiness = self.calc_happiness(arrangement)
            max_happiness = max(max_happiness, happiness)
        print(max_happiness)

    def add_me(self):
        self.guests['Me'] = {}
        for guest in self.guests:
            self.guests['Me'][guest] = 0
            self.guests[guest]['Me'] = 0

    def recur_arrangement(self, arrangement):
        for guest in self.guests:
            if guest not in arrangement:
                new_arrangement = arrangement.copy()
                new_arrangement.append(guest)
                self.recur_arrangement(new_arrangement)
        if len(arrangement) == len(self.guests):
            self.arrangements.append(arrangement)

    def calc_happiness(self, arrangement):
        happiness = 0
        for i in range(1, len(arrangement) - 1):
            happiness += self.guests[arrangement[i]][arrangement[i - 1]]
            happiness += self.guests[arrangement[i]][arrangement[i + 1]]
        happiness += self.guests[arrangement[0]][arrangement[1]]
        happiness += self.guests[arrangement[0]][arrangement[-1]]
        happiness += self.guests[arrangement[-1]][arrangement[-2]]
        happiness += self.guests[arrangement[-1]][arrangement[0]]
        return happiness


if __name__ == '__main__':
    Day13().solve()
