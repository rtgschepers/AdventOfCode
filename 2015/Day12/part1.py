import re

line = open('input.txt').readline()
print(sum([int(x) for x in re.findall(r'-*\d+', line)]))
