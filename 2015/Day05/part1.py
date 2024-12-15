import re

nice = 0
for line in [x.rstrip() for x in open('input.txt')]:
    a = len(re.findall(r'[aeiou]', line)) >= 3  # Contains at least 3 vowels
    b = len(re.findall(r'(.)\1', line)) > 0  # Contains at least one double
    c = len(re.findall(r'ab|cd|pq|xy', line)) == 0  # Does not contain forbidden
    if a and b and c:
        nice += 1
print(nice)
