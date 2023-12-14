from time import time


def step(r_boulders, s_boulders, f_size, direction):
    new_r_boulders = set()
    for i in range(f_size):
        stop = 0
        for j in range(f_size):
            if direction == 'n':
                if (j, i) in r_boulders:
                    new_r_boulders.add((stop, i))
                    stop += 1
                elif (j, i) in s_boulders:
                    stop = j + 1
            if direction == 's':
                if (f_size-j-1, i) in r_boulders:
                    new_r_boulders.add((f_size-1-stop, i))
                    stop += 1
                elif (f_size-j-1, i) in s_boulders:
                    stop = j+1
            if direction == 'w':
                if (i, j) in r_boulders:
                    new_r_boulders.add((i, stop))
                    stop += 1
                elif (i, j) in s_boulders:
                    stop = j + 1
            if direction == 'e':
                if (i, f_size-1-j) in r_boulders:
                    new_r_boulders.add((i, f_size-1-stop))
                    stop += 1
                elif (i, f_size-j-1) in s_boulders:
                    stop = j + 1
    return new_r_boulders


def step2(r_boulders, s_boulders, f_size, direction):
    change = {'n': (-1, 0), 's': (1, 0), 'w': (0, -1), 'e': (0, 1)}[direction]
    sorting = {'n': (1, f_size), 's': (-1, f_size), 'w': (f_size, 1), 'e': (f_size, -1)}[direction]
    r_boulders = sorted(r_boulders, key=(lambda x: (x[0] * sorting[0] + x[1] * sorting[1])))
    for index, coord in enumerate(r_boulders):
        new_coord = (coord[0] + change[0], coord[1] + change[1])
        while ((0 <= new_coord[0] < f_size) and (0 <= new_coord[1] < f_size)
               and (new_coord not in s_boulders) and (new_coord != r_boulders[index - 1])):
            coord = new_coord
            new_coord = (coord[0] + change[0], coord[1] + change[1])
        r_boulders[index] = coord
    return r_boulders


def new_round(r_boulders, s_boulders, f_size):
    r_boulders, s_boulders = set(r_boulders), set(s_boulders)
    r_boulders = step(r_boulders, s_boulders, f_size, 'n')
    r_boulders = step(r_boulders, s_boulders, f_size, 'w')
    r_boulders = step(r_boulders, s_boulders, f_size, 's')
    r_boulders = step(r_boulders, s_boulders, f_size, 'e')
    return r_boulders

def new_round2(r_boulders, s_boulders, f_size):
    r_boulders, s_boulders = list(r_boulders), set(s_boulders)
    r_boulders = step2(r_boulders, s_boulders, f_size, 'n')
    r_boulders = step2(r_boulders, s_boulders, f_size, 'w')
    r_boulders = step2(r_boulders, s_boulders, f_size, 's')
    r_boulders = step2(r_boulders, s_boulders, f_size, 'e')
    return r_boulders


def weight(r_boulders, f_size):
    total = 0
    for (i, j) in r_boulders:
        total += f_size-i
    return total

def print_new(r_boulders, s_boulders, f_size):
    for i in range(f_size):
        print(' ', end='')
        for j in range(f_size):
            if (i, j) in r_boulders:
                print('O', end='')
            elif (i, j) in s_boulders:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


lines = [list(line) for line in open('input.txt', 'r').read().split('\n') if line]
total = 0
for i in range(len(lines[0])):
    stop = len(lines)
    for j in range(len(lines)):
        if lines[j][i] == 'O':
            total += stop
            stop -= 1
        elif lines[j][i] == '#':
            stop = len(lines) - 1 - j
print(f"Part 1: {total}")

r_boulders = set()
s_boulders = set()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'O':
            r_boulders.add((i, j))
        elif lines[i][j] == '#':
            s_boulders.add((i, j))

f_size = len(lines)
assert f_size == len(lines[1])

start = time()
prev = {}
for i in range(1, 1_000_000_001):
    r_boulders = tuple(new_round(tuple(r_boulders), tuple(s_boulders), f_size))
    hash_val = hash(r_boulders)
    if hash_val in prev.keys():
        last = prev[hash_val]
        togo = (1_000_000_000 - i) % (i-last)
        for i in range(togo):
            r_boulders = tuple(new_round(tuple(r_boulders), tuple(s_boulders), f_size))
        print(f"Part 2: {weight(r_boulders, f_size)}")
        break
    prev[hash_val] = i
print(f"Time: {time()-start}")

r_boulders = set()
s_boulders = set()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == 'O':
            r_boulders.add((i, j))
        elif lines[i][j] == '#':
            s_boulders.add((i, j))

start = time()
prev = {}
r_boulders = sorted(r_boulders, key=(lambda x: (x[0] + x[1] * f_size)))
for i in range(1, 1_000_000_001):
    r_boulders = tuple(new_round2(r_boulders, s_boulders, f_size))
    hash_val = hash(r_boulders)
    if hash_val in prev.keys():
        last = prev[hash_val]
        togo = (1_000_000_000 - i) % (i-last)
        for i in range(togo):
            r_boulders = tuple(new_round2(r_boulders, s_boulders, f_size))
        print(f"Part 2: {weight(r_boulders, f_size)}")
        break
    prev[hash_val] = i
print(f"Time: {time()-start}")
