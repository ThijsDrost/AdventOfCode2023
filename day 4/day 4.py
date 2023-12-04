loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2023\day 4\input.txt'

# %% First part
value = 0
with open(loc, 'r') as file:
    for line in file:
        line = line.removesuffix('\n')
        winners, values = line.split(': ')[1].split(' | ')
        winners = set((int(x) for x in winners.split(' ') if x != ''))
        if len(winners) != 10:
            print('help')
        values = set((int(x) for x in values.split(' ') if x != ''))
        if len(values) != 25:
            print('help')
        print(values.intersection(winners))
        if (overlap := len(values.intersection(winners))) != 0:
            value += 2**(overlap - 1)

# %% Second part
value = 0
with open(loc, 'r') as file:
    file_length = len(file.readlines())

nums = [1 for _ in range(file_length)]
with open(loc, 'r') as file:
    for index, line in enumerate(file):
        line = line.removesuffix('\n')
        winners, values = line.split(': ')[1].split(' | ')
        winners = set((int(x) for x in winners.split(' ') if x != ''))
        values = set((int(x) for x in values.split(' ') if x != ''))
        for i in range(1, len(values.intersection(winners))+1):
            nums[index + i] += nums[index]

print(sum(nums))
