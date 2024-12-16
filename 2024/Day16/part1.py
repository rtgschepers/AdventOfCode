from timeit import timeit
from typing import List


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Node:
    def __init__(self, pos: Position, parent=None):
        self.parent = parent
        self.pos = pos

    def __eq__(self, other):
        return self.pos == other.pos


class Day16:
    grid = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self):
        for line in [x.rstrip() for x in open('test.txt')]:
            self.grid.append(list(line))
            if line.find('S') > -1:
                self.start = Node(Position(line.index('S'), len(self.grid) - 1))
            if line.find('E') > -1:
                self.end = Node(Position(line.index('E'), len(self.grid) - 1))

    def solve(self):
        closed_list: List[Node] = []
        open_list: List[Node] = [self.start]

        while len(open_list):
            cur_node = self.get_next_node(open_list)
            open_list.remove(cur_node)
            closed_list.append(cur_node)

            if cur_node == self.end:
                self.end = cur_node
                break

            for dx, dy in self.directions:
                new_node = Node(Position(cur_node.pos.x + dx, cur_node.pos.y + dy), cur_node)

                if new_node in closed_list or self.grid[new_node.pos.y][new_node.pos.x] == '#':
                    continue

                if new_node not in open_list:
                    open_list.append(new_node)

        path = []
        current: Node = self.end
        while current is not None:
            path.append((current.pos.x, current.pos.y))
            current = current.parent
        path = path[::-1]
        pass

    def get_next_node(self, open_list) -> (int, int):
        low_i = len(open_list) - 1
        low_f = 999999

        for i, node in enumerate(open_list):
            g = pow(abs(self.start.pos.x - node.pos.x), 2) + pow(abs(self.start.pos.y - node.pos.y), 2)
            h = pow(abs(self.end.pos.x - node.pos.x), 2) + pow(abs(self.end.pos.y - node.pos.y), 2)
            if g + h < low_f:
                low_f + g + h
                low_i = i

        return open_list[low_i]


if __name__ == '__main__':
    time = timeit(lambda: Day16().solve(), number=1)
    print(f'Execution time: {time:.4f}')
