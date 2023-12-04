import re

loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2023\day 3\input.txt'

# %% First part
spacer = r'.'
number_sum = 0

with open(loc, 'r') as file:
    lines = ''
    for line in file:
        lines += line.removesuffix('\n')
        length = len(line) - 1

    relative_indexes = [-1, 1, -length, length, -length-1, -length+1, length-1, length+1]

    values = {}
    for reg in re.finditer(r'\d+', lines):
        for i in range(reg.start(), reg.end()):
            values[i] = (int(reg.group()), list(range(reg.start(), reg.end())))

    index = 0
    for reg in re.finditer(rf'[^0-9{spacer}]', lines):
        skip_values = []
        for i in relative_indexes:
            if ((reg.start()+i) not in skip_values) and ((reg.start()+i) in values.keys()):
                number_sum += values[reg.start()+i][0]
                skip_values.extend(values[reg.start()+i][1])

print(number_sum)

# %%
spacer = r'.'
gear = '\*'
gear_ratio = 0

with open(loc, 'r') as file:
    index = 0
    for reg in re.finditer(rf'{gear}', lines):
        skip_values = []
        gear_values = []
        for i in relative_indexes:
            if ((reg.start()+i) not in skip_values) and ((reg.start()+i) in values.keys()):
                gear_values.append(values[reg.start()+i][0])
                skip_values.extend(values[reg.start()+i][1])
        if len(gear_values) == 2:
            gear_ratio += gear_values[0] * gear_values[1]

print(gear_ratio)
