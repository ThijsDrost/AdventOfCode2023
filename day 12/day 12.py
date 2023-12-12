import functools


@functools.cache
def possible(string, lister: tuple):
    total = 0
    if len(lister) == 0:
        if string.count('#') == 0:
            return 1
        else:
            return 0
    if len(string) < sum(lister):
        return 0
    if (len(string) == lister[0]) and (string.count('.') == 0) and (len(lister) == 1):
        return 1
    for i in range(len(string)-lister[0]+1):
        if (string[i:i+lister[0]].count('.') == 0) and (i+lister[0] == len(string) or string[i+lister[0]] != '#') and (string[:i].count('#') == 0):
            total += possible(string[i+lister[0]+1:], lister[1:])
    return total


total = 0
lines = [line.split(' ') for line in open('input.txt', 'r').read().split('\n') if line]
for index, (line, values) in enumerate(lines):
    total += possible(line, tuple([int(value) for value in values.split(',')]))
print(f'part 1: {total}')

total = 0
lines = [line.split(' ') for line in open('input.txt', 'r').read().split('\n') if line]
for index, (line, values) in enumerate(lines):
    line = '?'.join([line for _ in range(5)])
    values = ','.join([values for _ in range(5)])
    total += possible(line, tuple([int(value) for value in values.split(',')]))
print(f'part 2: {total}')
