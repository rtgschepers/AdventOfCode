def main():
    total = 0
    for line in [x.rstrip() for x in open('input.txt')]:
        rows = [[int(c) for c in line.split(' ')]]
        while True:
            rows.append(get_increments(rows[-1]))
            if len(set(rows[-1])) == 1:
                break

        for i in range(len(rows) - 1, 0, -1):
            rows[i - 1].insert(0, rows[i - 1][0] - rows[i][0])
        total += rows[0][0]
    print(total)


def get_increments(nums):
    increments = []
    for i in range(len(nums) - 1):
        increments.append(nums[i + 1] - nums[i])
    return increments


if __name__ == '__main__':
    main()
