import re

nice = 0
for line in [x.rstrip() for x in open('input.txt')]:
    a = len(re.findall(r'(\w)(\w)\1', line)) > 0  # Contains at least 3 vowels
    b = len(re.findall(r'(\w\w).*\1', line)) > 0  # Contains repeating character pair
    if a and b:
        nice += 1
print(nice)
