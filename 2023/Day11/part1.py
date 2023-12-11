import numpy as np


def main():
    universe = []
    for line in [x.rstrip() for x in open('test.txt')]:
        universe.append(list(line))
    universe = np.array(universe)
    universe = expand_universe(universe)

    galaxies = np.argwhere(universe == '#')

    distances = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distances.append(abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1]))
    print(sum(distances))


def expand_universe(universe):
    temp = universe.copy()
    inserted = 0
    for i in range(len(universe)):
        if len(np.unique(universe[i, :])) == 1:
            temp = np.insert(temp, i + inserted, np.full(len(temp[0]), '.', dtype=str), 0)
            inserted += 1
    inserted = 0
    for i in range(len(universe[0])):
        if len(np.unique(universe[:, i])) == 1:
            temp = np.insert(temp, i + inserted, np.full(len(temp), '.', dtype=str), 1)
            inserted += 1
    return temp


if __name__ == '__main__':
    main()
