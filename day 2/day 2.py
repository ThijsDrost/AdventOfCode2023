import re

loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2023\day 2\input.txt'

game_sum = 0
power_sum = 0
red_max = 12
green_max = 13
blue_max = 14

vals = []
with open(loc, 'r') as file:
    for line in file:
        line = line.removesuffix('\n')
        number, values = line.removeprefix('Game').split(':')
        blues = int(max(re.findall(r'(\d+) blue', values), default=0, key=int))
        reds = int(max(re.findall(r'(\d+) red', values), default=0, key=int))
        greens = int(max(re.findall(r'(\d+) green', values), default=0, key=int))
        vals.append((number, reds, greens, blues))
        power_sum += blues*reds*greens
        if (blues > blue_max) or (reds > red_max) or (greens > green_max):
            continue
        game_sum += int(number)

print(game_sum)
print(power_sum)
