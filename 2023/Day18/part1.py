def main():
    x = [0]
    y = [0]
    for line in [x.rstrip() for x in open('input.txt')]:
        direction, length, color = line.split(' ')
        match direction:
            case 'R':
                x.append(x[-1] + int(length))
                y.append(y[-1])
            case 'L':
                x.append(x[-1] - int(length))
                y.append(y[-1])
                pass
            case 'D':
                x.append(x[-1])
                y.append(y[-1] + int(length))
                pass
            case 'U':
                x.append(x[-1])
                y.append(y[-1] - int(length))
                pass
    print(shoelace(x, y))


def shoelace(x, y):
    n = len(x)
    area = 0

    for i in range(n - 1):
        area += x[i] * y[i + 1] - x[i + 1] * y[i]

    area += x[n - 1] * y[0] - x[0] * y[n - 1]
    area = abs(area) / 2.0

    edge_lengths = [((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** 0.5 for i in range(n - 1)]
    edge_lengths.append(((x[n - 1] - x[0]) ** 2 + (y[n - 1] - y[0]) ** 2) ** 0.5)

    area += sum(edge_lengths) / 2.0

    return area + 1


if __name__ == '__main__':
    main()
