import argparse
import os
import webbrowser
from pathlib import Path

import requests


def main():
    parser = argparse.ArgumentParser(description='AOC management command.')

    parser.add_argument('year', help='Year of the event, e.g. 2015',
                        choices=generate_years(), metavar='year')
    parser.add_argument('day', help='Day of the puzzle, e.g. 5 ',
                        choices=generate_days(), metavar='day')

    args = parser.parse_args()
    create_new_puzzle_files(args.year, args.day)


def generate_years():
    from datetime import datetime
    return [str(x) for x in range(2015, datetime.now().year + 1)]


def generate_days():
    return [str(x) for x in range(1, 26)]


def create_new_puzzle_files(year, day):
    url = 'https://adventofcode.com/{}/day/{}'.format(year, day)
    webbrowser.open(url, new=0, autoraise=True)

    path = '{}/Day{}'.format(year, day)
    Path(path).mkdir(parents=True, exist_ok=True)

    parts = [1, 2]
    for part in parts:
        file_path = '{}/part{}.py'.format(path, part)
        if not Path(file_path).is_file():
            with open(file_path, 'w') as f:
                f.write('for line in [x.rstrip() for x in open(\'test.txt\')]:{0}    break{0}'.format(os.linesep))

    file_path = '{}/test.txt'.format(path)
    if not Path(file_path).is_file():
        with open(file_path, 'w') as f:
            f.write('')

    file_path = '{}/input.txt'.format(path)
    if not Path(file_path).is_file():
        puzzle_input = get_puzzle_input(url)
        with open(file_path, 'w') as f:
            f.write(puzzle_input)


def get_puzzle_input(url):
    url = '{}/input'.format(url)
    from config import SESSION
    cookies = {'session': SESSION}
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    response = requests.get(url, cookies=cookies, headers=headers)
    return response.text.strip()


if __name__ == '__main__':
    main()
