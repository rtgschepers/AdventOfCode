class Day9:
    locations = {}
    routes = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            cities, distance = line.split(' = ')
            start, end = cities.split(' to ')

            for city in [start, end]:
                if city not in self.locations:
                    self.locations[city] = {}

            self.locations[start][end] = distance
            self.locations[end][start] = distance

    def solve(self):
        for location in self.locations:
            self.recur_route([location])

        longest_len = 0
        for route in self.routes:
            route_len = 0
            for i in range(len(route) - 1):
                route_len += int(self.locations[route[i]][route[i + 1]])
            longest_len = max(longest_len, route_len)
        print(longest_len)

    def recur_route(self, route):
        for location in self.locations:
            if location not in route:
                new_route = route.copy()
                new_route.append(location)
                self.recur_route(new_route)
        if len(route) == len(self.locations):
            self.routes.append(route)


if __name__ == '__main__':
    Day9().solve()
