loc = r'input.txt'


def read_and_map(file, old):
    new = [-1 for _ in range(len(old))]
    for line in file:
        if line == '\n':
            break
        new_start, old_start, range_len = map(int, line.removesuffix('\n').split())
        for i in range(len(new)):
            if old_start <= old[i] < old_start + range_len:
                new[i] = new_start + old[i] - old_start
    for i in range(len(new)):
        if new[i] == -1:
            new[i] = old[i]
    return new


with open(loc, 'r') as file:
    new = list(map(int, file.readline().removesuffix('\n').split(':')[1].split()))
    file.readline()
    while True:
        if not file.readline():
            break
        new = read_and_map(file, new)

print(f'part 1: {min(new)}')


# %% part 2
def read_and_map(file, ranges):
    new = []
    for line in file:
        ranges_old = []
        if line == '\n':
            break
        new_start, old_start, range_len = map(int, line.removesuffix('\n').split())
        for start, stop in ranges:
            dv = new_start-old_start
            if stop < old_start:
                ranges_old.append((start, stop))
                continue
            if start > old_start + range_len:
                ranges_old.append((start, stop))
                continue
            if start < old_start:
                ranges_old.append((start, old_start))
                if stop <= old_start + range_len:
                    new.append((new_start, stop+dv))
                    continue
                if stop > old_start + range_len:
                    new.append((new_start, new_start+range_len))
                    ranges_old.append((old_start+range_len, stop))
                    continue
            if start >= old_start:
                if stop <= old_start + range_len:
                    new.append((start+dv, stop+dv))
                    continue
                if stop > old_start + range_len:
                    new.append((new_start+start-old_start, new_start+range_len))
                    ranges_old.append((old_start+range_len, stop))
                    continue
        ranges = ranges_old
    new.extend(ranges)
    return new


with open(loc, 'r') as file:
    values = list(map(int, file.readline().removesuffix('\n').split(':')[1].split()))
    ranges = []
    for i in range(len(values)//2):
        ranges.append((values[2*i], values[2*i]+values[2*i+1]))
    file.readline()
    while True:
        if not file.readline():
            break
        ranges = read_and_map(file, ranges)

print(f'part 2: {min([r[0] for r in ranges])}')
