import numpy as np


def main():
    universe = []
    for line in [x.rstrip() for x in open('input.txt')]:
        universe.append(list(line))
    universe = np.array(universe)

    galaxies = np.argwhere(universe == '#')
    empty_rows = np.where(np.all(universe == '.', axis=1))[0]
    empty_cols = np.where(np.all(universe == '.', axis=0))[0]

    distances = []
    expansion = 1000000
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            y1, x1, y2, x2 = np.concatenate((galaxies[i], galaxies[j]))

            empty_rows_between = count_empty_space(empty_rows, y1, y2)
            empty_cols_between = count_empty_space(empty_cols, x1, x2)

            h_dist = abs(x2 - x1)
            h_dist += empty_cols_between * expansion - empty_cols_between
            v_dist = abs(y2 - y1)
            v_dist += empty_rows_between * expansion - empty_rows_between

            distances.append(h_dist + v_dist)
    print(sum(distances))


def count_empty_space(empty_space, a, b):
    a, b = sorted((a, b))
    empty_space_between = 0

    if b - a > 1:
        for i in empty_space:
            if a < i < b:
                empty_space_between += 1
    return empty_space_between


if __name__ == '__main__':
    main()
