from itertools import combinations
import numpy as np

expanding_factor = 1000000
lines = [line for line in open('input.txt', 'r').read().split('\n') if line]
values = np.array([list(map({'.': 0, '#': 1}.get, line)) for line in lines])
galaxies = np.argwhere(values == 1)

expanding_values = np.zeros(galaxies.shape, dtype=int)

for index in np.argwhere(np.sum(values, axis=1) == 0):
    expanding_values[galaxies[:, 0] > index, 0] += 1

for index in np.argwhere(np.sum(values, axis=0) == 0):
    expanding_values[galaxies[:, 1] > index, 1] += 1

total = 0
total2 = 0
for pair in combinations(np.arange(len(galaxies)), 2):
    total += np.sum(np.abs((galaxies[pair[0]]+expanding_values[pair[0]])-(galaxies[pair[1]]+expanding_values[pair[1]])))
    total2 += np.sum(
        np.abs((galaxies[pair[0]] + (expanding_factor-1)*expanding_values[pair[0]])
               - (galaxies[pair[1]] + (expanding_factor-1)*expanding_values[pair[1]])))
print(f'part 1: {total}')
print(f'part 2: {total2}')
