import re
import math

loc = 'input.txt'
with open(loc, 'r') as file:
    times = list(map(int, re.findall(r'(\d+)', file.readline())))
    distances = list(map(int, re.findall(r'(\d+)', file.readline())))

total = 1
for t, d in zip(times, distances):
    D = math.sqrt(t**2 - 4*(d+1e-10))  # 1e-10 sice
    total *= math.floor((t + D)/2) - math.ceil((t - D)/2) + 1
print(total)

t = int(''.join(map(str, times)))
d = int(''.join(map(str, distances)))
D = math.sqrt(t**2 - 4*(d+1e-10))
print(math.floor((t + D)/2) - math.ceil((t - D)/2) + 1)
