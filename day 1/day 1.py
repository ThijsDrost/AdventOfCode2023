import numpy as np

with open(r'C:\Users\20222772\PycharmProjects\AdventOfCode2023\day 1\input.txt', 'r') as file:
    lines = [line.removesuffix('\n') for line in file]

# %%
total = 0
for index, line in enumerate(lines):
    num_str = ''
    for letter in line:
        if letter.isdigit():
            num_str += letter
            break
    for letter in line[::-1]:
        if letter.isdigit():
            num_str += letter
            break
    total += int(num_str)
print(total)

# %%
str_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
total = 0
for index, line in enumerate(lines):
    values = {}
    for index2, num in enumerate(str_numbers):
        if (i := line.find(num)) != -1:
            values[i] = index2 + 1

    min_index = min(values.keys()) if len(values) != 0 else None
    for letter in line[:min_index]:
        if letter.isdigit():
            number = 10 * int(letter)
            break
    else:
        number = 10 * values[min_index]

    values = {}
    for index2, num in enumerate(str_numbers):
        if (i := line[::-1].find(num[::-1])) != -1:
            values[len(line) - i - 1] = (index2 + 1)
    max_index = max(values.keys()) if len(values) != 0 else None

    for letter in line[-1:max_index:-1]:
        if letter.isdigit():
            number += int(letter)
            break
    else:
        number += values[max_index]
    total += number

print(total)


