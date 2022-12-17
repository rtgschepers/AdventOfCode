for line in [x.replace('\n', '') for x in open('input.txt')]:
    for i in range(len(line)):
        sub = [*line[i:i + 4]]
        if len(sub) == len(set(sub)):
            print(i + 4)
            break
