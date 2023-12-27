import re


class Day15:
    properties = []
    ingredients = {}
    ratios = {}

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            ingredient, properties = line.split(': ')
            if ingredient not in self.ingredients:
                self.ingredients[ingredient] = {}

            self.properties = re.findall(r'[A-z]+', properties)
            values = re.findall(r'-*\d+', line)
            for i in range(len(self.properties)):
                self.ingredients[ingredient][self.properties[i]] = int(values[i])

        for ingredient in self.ingredients:
            self.ratios[ingredient] = 100 / len(self.ingredients)

    def solve(self):
        high_score = 0
        for a in range(1, 101):
            for b in range(1, 101 - a):
                for c in range(1, 101 - a - b):
                    d = 100 - a - b - c
                    if d >= 1:
                        self.ratios['Candy'], self.ratios['Chocolate'], self.ratios['Sprinkles'], self.ratios[
                            'Sugar'] = a, b, c, d
                        high_score = max(high_score, self.calc_score())
        print(high_score)

    def calc_score(self):
        score = 1
        for _property in self.properties:
            if _property == 'calories':
                continue

            property_score = 0
            for ingredient, ratio in self.ratios.items():
                property_score += self.ingredients[ingredient][_property] * ratio
            score *= max(property_score, 0)
        return score


if __name__ == '__main__':
    Day15().solve()
