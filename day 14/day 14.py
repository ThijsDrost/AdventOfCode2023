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


def new_round(r_boulders, s_boulders, f_size):
    r_boulders, s_boulders = set(r_boulders), set(s_boulders)
    r_boulders = step(r_boulders, s_boulders, f_size, 'n')
    r_boulders = step(r_boulders, s_boulders, f_size, 'w')
    r_boulders = step(r_boulders, s_boulders, f_size, 's')
    r_boulders = step(r_boulders, s_boulders, f_size, 'e')
    return r_boulders


def weight(r_boulders, f_size):
    total = 0
    for (i, j) in r_boulders:
        total += f_size-i
    return total


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
