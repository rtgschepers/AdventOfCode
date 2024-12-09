import re
from collections import deque
from timeit import timeit

from tqdm import tqdm


class Day7:
    _input = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            self._input.append([x for x in re.findall(r'\d+', line)])
            pass

    def solve(self):
        answer = 0
        for eq in tqdm(self._input):
            target = int(eq[0])
            numbers = eq[1:]
            answer += self.generate_formulas('+'.join(numbers), target)
        print(answer)

    def generate_formulas(self, formula: str, target: int) -> int:
        operations = ['*', '|']
        queue = deque([formula])
        seen = set()

        while queue:
            cur_formula = queue.popleft()
            if cur_formula in seen:
                continue
            seen.add(cur_formula)

            if self.eval_ltr(cur_formula) == target:
                return target

            for match in re.finditer(r'[+]', cur_formula):
                i = match.start()
                for op in operations:
                    new_formula = f'{cur_formula[:i]}{op}{cur_formula[i + 1:]}'
                    if new_formula not in seen:
                        queue.append(new_formula)
        return 0

    def eval_ltr(self, formula: str) -> int:
        symbols = re.findall(r'\d+|\*|\+|\|', formula)
        ans = int(symbols[0])
        for x in range(1, len(symbols), 2):
            match symbols[x]:
                case '+':
                    ans += int(symbols[x + 1])
                case '*':
                    ans *= int(symbols[x + 1])
                case '|':
                    ans = int(str(ans) + symbols[x + 1])
        return ans


if __name__ == '__main__':
    time = timeit(lambda: Day7().solve(), number=1)
    print(f'Execution time: {time:.4f}')
