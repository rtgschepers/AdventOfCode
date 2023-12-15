import numpy as np


def main():
    platform = []
    for line in [x.rstrip() for x in open('input.txt')]:
        platform.append(list(line))
    platform = np.asarray(platform)

    for col_index in range(platform.shape[1]):
        col = platform[:, col_index]
        i = 1
        while i < len(col):
            if col[i - 1] == '.' and col[i] == 'O':
                col[i], col[i - 1] = col[i - 1], col[i]
                i = max(0, i - 2)
            i += 1
        platform[:, col_index] = col

    total = 0
    for i in range(len(platform)):
        total += (len(platform) - i) * np.count_nonzero(platform[i] == 'O')
    print(total)


if __name__ == '__main__':
    main()
