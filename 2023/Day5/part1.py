import re


def calculate_destination(value, source, destination, map_range):
    changed = False
    if source <= value < source + map_range:
        value += destination - source
        changed = True
    return value, changed


def main():
    with open('input.txt') as f:
        content = f.read()

    sections = content.split('\n\n')
    seeds = [int(x) for x in re.findall(r'\d+', sections[0])]
    answers = []

    for seed in seeds:
        value = seed
        for section in sections[1:]:
            maps = [[int(y) for y in x.split(' ')] for x in section.split('\n')[1:]]
            for map_info in maps:
                value, changed = calculate_destination(value, map_info[1], map_info[0], map_info[2])
                if changed:
                    break
        answers.append({'seed': seed, 'location': value})

    print(answers)
    print(min([x['location'] for x in answers]))


main()
