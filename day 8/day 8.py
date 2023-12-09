import re
import math

lines = [line for line in open("input.txt").read().split("\n") if line]
directions = lines[0]
nodes = {node: direction for node, *direction in map(lambda line: re.findall(r'([A-Z]{3})', line), lines[1:])}
locations = [node for node in nodes.keys() if node[-1] == 'A']

starts = locations.copy()
result = 1
for i in range(len(locations)):
    index = 0
    while True:
        locations[i] = nodes[locations[i]]['LR'.index(directions[index % len(directions)])]
        index += 1
        if locations[i][-1] == 'Z':
            if starts[i] == 'AAA':
                print(f'part 1: {index}')
            result = math.lcm(result, index)
            break
print(f'part 2: {result}')
