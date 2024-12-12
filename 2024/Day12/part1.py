from collections import deque
from timeit import timeit


class Day12:
    garden = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self.garden.append(list(line))

    def solve(self):
        processed = []
        plots = {}

        for y in range(len(self.garden)):
            for x in range(len(self.garden[0])):
                if (x, y) in processed:
                    continue

                cur_plot = self.garden[y][x]
                cur_plot_id = len(plots)
                plots[cur_plot_id] = {'area': 0, 'perimeter': 0}

                plot = deque([(x, y)])
                while len(plot):
                    cur_x, cur_y = plot.popleft()
                    if (cur_x, cur_y) in processed:
                        continue

                    plots[cur_plot_id]['area'] += 1
                    processed.append((cur_x, cur_y))

                    for dx, dy in self.directions:
                        new_x, new_y = cur_x + dx, cur_y + dy

                        if not (0 <= new_x < len(self.garden[0])) or not (0 <= new_y < len(self.garden)):
                            plots[cur_plot_id]['perimeter'] += 1
                            continue

                        if self.garden[new_y][new_x] != cur_plot:
                            plots[cur_plot_id]['perimeter'] += 1
                        elif (new_x, new_y) not in plot and (new_x, new_y) not in processed:
                            plot.append((new_x, new_y))
        ans = 0
        for plot in plots.values():
            ans += plot['area'] * plot['perimeter']
        print(ans)


if __name__ == '__main__':
    time = timeit(lambda: Day12().solve(), number=1)
    print(f'Execution time: {time:.4f}')
