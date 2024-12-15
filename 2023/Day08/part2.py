import math

import sympy.ntheory as nt


def get_prime_factors(number):
    primes = []
    while number != 1:
        divisor = 2
        while number % divisor != 0:
            divisor = nt.nextprime(divisor)
        primes.append(divisor)
        number /= divisor
        if nt.isprime(number):
            primes.append(number)
            break
    return primes


maps = {}
cur_pos = []
with open('input.txt') as f:
    instructions = f.readline().strip()
    f.readline()

    for line in f.readlines():
        parts = line.strip().split(' = ')
        if parts[0][-1] == 'A':
            cur_pos.append(parts[0])

        lr = parts[1].replace('(', '').replace(')', '').split(', ')
        maps[parts[0]] = {
            'L': lr[0],
            'R': lr[1],
        }

loop_lengths = []
for i in range(len(cur_pos)):
    steps = 0
    while cur_pos[i][-1] != 'Z':
        step = instructions[steps % len(instructions)]
        cur_pos[i] = maps[cur_pos[i]][step]
        steps += 1
    loop_lengths.append(steps)

prime_factors = []
for length in loop_lengths:
    prime_factors.append(get_prime_factors(length))
prime_factors = list(set([num for row in prime_factors for num in row]))
print(math.prod(prime_factors))
