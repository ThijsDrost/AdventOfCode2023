import re
loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2023\day 4\input.txt'

# %%
with open(loc, 'r') as file:
    file_length = len(file.readlines())

value = 0
nums = [1 for _ in range(file_length)]
with open(loc, 'r') as file:
    for index, line in enumerate(file):
        line = line.removesuffix('\n')
        winners, values = line.split(':')[1].split('|')
        winners = set((int(x) for x in winners.split()))
        values = set((int(x) for x in values.split()))
        # first part
        if (overlap := len(values.intersection(winners))) != 0:
            value += 2**(overlap - 1)
        # second part
        for i in range(1, len(values.intersection(winners))+1):
            nums[index + i] += nums[index]

print(value)
print(sum(nums))
