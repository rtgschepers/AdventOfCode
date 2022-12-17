import re

stacks = {}
lines = [x.replace('\n', '') for x in open('input.txt')]
split = lines.index('')
indices = lines[split - 1]

for i in range(0, len(indices)):
    if indices[i] != ' ':
        stacks[indices[i]] = []
        for line in reversed(lines[:split - 1]):
            if i < len(line) and line[i] != ' ':
                stacks[indices[i]].append(line[i])

for line in lines[split + 1:]:
    commands = re.findall(r'\d+', line)
    to_move = stacks[commands[1]][int(commands[0]) * -1:]
    del stacks[commands[1]][int(commands[0]) * -1:]
    stacks[commands[2]].extend(to_move)

output = ''
for stack in stacks.items():
    output += stack[1][len(stack[1]) - 1]
print(output)
